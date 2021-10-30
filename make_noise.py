import argparse
import numpy as np
import torch
from utils import *
import PIL.Image as pil_image

parser = argparse.ArgumentParser()
parser.add_argument('--image-file', type=str, required=True)
parser.add_argument("--test_noiseL", type=float, default=25, help='noise level used on test set')
opt = parser.parse_args()

def main():

    print('Loading Image\n')
    image = pil_image.open(opt.image_file).convert('RGB')

    image = np.expand_dims(np.array(image).astype(np.float32).transpose([2, 0, 1]), 0) / 255.0
    ISource = torch.from_numpy(image)

    noise = torch.FloatTensor(ISource.size()).normal_(mean=0, std=opt.test_noiseL / 255.)

    INoisy = (ISource + noise).squeeze(0)

    output = pil_image.fromarray(denormalize(INoisy).permute(1, 2, 0).byte().cpu().numpy())
    output.save(opt.image_file.replace('.', '_add_noise.'))
    print('Make Image\n')
    
if __name__ == "__main__":
    main()
