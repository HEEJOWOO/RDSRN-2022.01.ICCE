import argparse
import os
import copy
import torch
from torch import nn
import torch.optim as optim
import torch.backends.cudnn as cudnn
from torch.utils.data.dataloader import DataLoader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm
from models import RDSRN
from datasets import TrainDataset, EvalDataset
from utils import AverageMeter, denormalize, calc_psnr, load_weights, convert_rgb_to_y
import torchsummary
from ptflops import get_model_complexity_info
from prettytable import PrettyTable
from torchstat import stat

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-file', type=str, required=True)
    parser.add_argument('--eval-file', type=str, required=True)
    parser.add_argument('--outputs-dir', type=str, required=True)
    parser.add_argument('--weights-file', type=str)
    parser.add_argument('--num-features', type=int, default=64)
    parser.add_argument('--growth-rate', type=int, default=64)
    parser.add_argument('--U', type=int, default=3)
    parser.add_argument('--scale', type=int, default=4)
    parser.add_argument('--patch-size', type=int, default=64)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--num-epochs', type=int, default=800)
    parser.add_argument('--num-workers', type=int, default=8)
    parser.add_argument('--num-channels', type=int, default=3)
    parser.add_argument('--seed', type=int, default=123)
    args = parser.parse_args()

    args.outputs_dir = os.path.join(args.outputs_dir, 'x{}'.format(args.scale))

    if not os.path.exists(args.outputs_dir):
        os.makedirs(args.outputs_dir)

    cudnn.benchmark = True
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    
    torch.manual_seed(args.seed)

    
    model = RDSRN(scale_factor=args.scale, num_channels=args.num_channels, num_features=args.num_features,growth_rate=args.growth_rate, U=args.U)
    
    
    macs, params = get_model_complexity_info(model, (3, 320, 180), as_strings=True,
                                           print_per_layer_stat=True, verbose=True)
    model.to(device)
    ###############################################################################
    #check params & macs
    print(model)
    print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
    print('{:<30}  {:<8}'.format('Number of parameters: ', params))
    print('Memory(GB) : %.3f'%(torch.cuda.memory_allocated(device)/1000/1000))
    ###############################################################################
    
    
    writer=SummaryWriter()

    if args.weights_file is not None:
        state_dict = model.state_dict()
        for n, p in torch.load(args.weights_file, map_location=lambda storage, loc: storage).items():
            if n in state_dict.keys():
                state_dict[n].copy_(p)
            else:
                raise KeyError(n)
    #Loss Function
    criterion = nn.L1Loss()
    #Optimizer
    optimizer = optim.Adam(model.parameters(), lr=args.lr)
    #DataLoader
    train_dataset = TrainDataset(args.train_file, patch_size=args.patch_size, scale=args.scale)
    train_dataloader = DataLoader(dataset=train_dataset,
                                  batch_size=args.batch_size,
                                  shuffle=True,
                                  num_workers=args.num_workers,
                                  pin_memory=True)
    eval_dataset = EvalDataset(args.eval_file)
    eval_dataloader = DataLoader(dataset=eval_dataset, batch_size=1)

    best_weights = copy.deepcopy(model.state_dict())
    best_epoch = 0
    best_psnr = 0.0
    #train
    for epoch in range(args.num_epochs):
        
        for param_group in optimizer.param_groups:
            param_group['lr'] = args.lr * (0.1 ** (epoch // int(args.num_epochs * 0.8)))

        model.train()
        epoch_losses = AverageMeter()

        with tqdm(total=(len(train_dataset) - len(train_dataset) % args.batch_size), ncols=80) as t:
            t.set_description('epoch: {}/{}'.format(epoch, args.num_epochs - 1))

            for data in train_dataloader:
                inputs, labels = data

                inputs = inputs.to(device)
                labels = labels.to(device)

                preds = model(inputs)

                loss = criterion(preds, labels)

                epoch_losses.update(loss.item(), len(inputs))

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                t.set_postfix(loss='{:.6f}'.format(epoch_losses.avg))
                t.update(len(inputs))
        writer.add_scalar('Loss-Epoch',epoch_losses.avg,epoch)
        if (epoch + 1) % 10 == 0:
            torch.save(model.state_dict(), os.path.join(args.outputs_dir, 'epoch_{}.pth'.format(epoch)))

        model.eval()
        epoch_psnr = AverageMeter()
        #val
        for data in eval_dataloader:
            inputs, labels = data

            inputs = inputs.to(device)
            labels = labels.to(device)

            with torch.no_grad():
                preds = model(inputs)

            preds = convert_rgb_to_y(denormalize(preds.squeeze(0)), dim_order='chw')
            labels = convert_rgb_to_y(denormalize(labels.squeeze(0)), dim_order='chw')

            preds = preds[args.scale:-args.scale, args.scale:-args.scale]
            labels = labels[args.scale:-args.scale, args.scale:-args.scale]

            epoch_psnr.update(calc_psnr(preds, labels), len(inputs))

        print('eval psnr: {:.2f}'.format(epoch_psnr.avg))
        writer.add_scalar('PSNR-Epoch',epoch_psnr.avg,epoch)
        if epoch_psnr.avg > best_psnr:
            best_epoch = epoch
            best_psnr = epoch_psnr.avg
            best_weights = copy.deepcopy(model.state_dict())

    print('best epoch: {}, psnr: {:.2f}'.format(best_epoch, best_psnr))
    torch.save(best_weights, os.path.join(args.outputs_dir, 'best.pth'))
