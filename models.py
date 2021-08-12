from torch import nn
import torch
import torch.nn.functional as F
from torch.nn.parameter import Parameter
class Scale(nn.Module):

    def __init__(self, init_value=1e-3):
        super().__init__()
        self.scale = nn.Parameter(torch.FloatTensor([init_value]))

    def forward(self, input):
        return input * self.scale
        
def mean_channels(F):
    assert(F.dim() == 4)
    spatial_sum = F.sum(3, keepdim=True).sum(2, keepdim=True)
    return spatial_sum / (F.size(2) * F.size(3))
    
def stdv_channels(F):
    assert(F.dim() == 4)
    F_mean = mean_channels(F)
    F_variance = (F - F_mean).pow(2).sum(3, keepdim=True).sum(2, keepdim=True) / (F.size(2) * F.size(3))
    return F_variance.pow(0.5)

class Dense_Layer(nn.Module):
    def __init__(self,i,grwoth_rate,wn):
        super(Dense_Layer, self).__init__()
        
        in_channels=grwoth_rate
        gc=grwoth_rate
        
        self.layer = nn.Sequential(wn(nn.Conv2d(in_channels + i * gc, gc,3, padding=1, bias=True)),nn.ReLU(True))
        
    def forward(self, x):
        return self.layer(x)

class refinement_layer(nn.Module):
    def __init__(self,distillation_rate,i,growth_rate,wn):
        super(refinement_layer, self).__init__()
        
        gr = growth_rate
        rf = growth_rate-(int(growth_rate*distillation_rate))
        
        self.layer = nn.Sequential(wn(nn.Conv2d(rf,rf*i,3,padding=3//2)),nn.ReLU(True),wn(nn.Conv2d(rf*i,rf,3,padding=3//2)))
        
    def forward(self, x):
        return self.layer(x)+x
        
class CCA(nn.Module):
    def __init__(self,num_features,wn):
        super(CCA, self).__init__()
        
        self.contrast = stdv_channels
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.conv_du = nn.Sequential(
            wn(nn.Conv2d(num_features, num_features // 16, 1, padding=0, bias=True)),
            nn.ReLU(inplace=True),
            wn(nn.Conv2d(num_features // 16, num_features, 1, padding=0, bias=True)),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        y =self.contrast(x)+self.avg_pool(x)
        y = self.conv_du(y)
        x = x*y
        return x
        
class RDB(nn.Module):

            
    def __init__(self, in_channels, growth_rate, num_layers,wn):
        super(RDB, self).__init__()
        wn = wn
        
        distillation_rate=0.5
        self.distilled_channels = int(growth_rate*0.5)
        self.remaining_channels = growth_rate-int(growth_rate*0.5)
        gc = growth_rate
        num_features = growth_rate
        
        self.layer1 = Dense_Layer(0,gc,wn)
        self.layer2 = Dense_Layer(1,gc,wn)
        self.layer3 = Dense_Layer(0,gc,wn)
        self.layer4 = Dense_Layer(1,gc,wn)
        
                
        self.refinement_layer_1 = refinement_layer(distillation_rate,3,growth_rate, wn)
        self.refinement_layer_2 = refinement_layer(distillation_rate,3,growth_rate, wn)
        self.refinement_layer_3 = refinement_layer(distillation_rate,4,growth_rate, wn)
        self.refinement_layer_4 = refinement_layer(distillation_rate,4,growth_rate, wn)
       
        
        self.CONCAT_FF_1=wn(nn.Conv2d(num_features*2,num_features,1))
        self.CONCAT_FF_2=wn(nn.Conv2d(num_features*3,num_features,1))
        
        self.CCA=CCA(num_features,wn)
        
        '''
        self.res_scale_1 = Scale(1)
        self.x_scale_1 = Scale(1)
        
        self.res_scale_2 = Scale(1)
        self.x_scale_2 = Scale(1)
        
        self.res_scale_5 = Scale(1)
        self.x_scale_5 = Scale(1)
        
        self.res_scale_6 = Scale(1)
        self.x_scale_6 = Scale(1)
        '''

    def forward(self, x, sfe_residual): 
        block_residual = x
        #####################################################################################################################################################################
        layer1 = self.layer1(x)+x 
        distilled_c1, remaining_c1 = torch.split(layer1, (self.distilled_channels, self.remaining_channels), dim=1) # 16 48
        refinement_layer_1 = self.refinement_layer_1(remaining_c1)
        concat1 = torch.cat([distilled_c1,refinement_layer_1],1)
        #####################################################################################################################################################################
        layer2 = self.layer2(torch.cat([x, concat1], 1))+concat1 # 128->64
        distilled_c2, remaining_c2 = torch.split(layer2, (self.distilled_channels, self.remaining_channels), dim=1) # 16 48
        refinement_layer_2 = self.refinement_layer_2(remaining_c2)
        concat2 = torch.cat([distilled_c2,refinement_layer_2],1)
        #####################################################################################################################################################################
        concat_save_1 = torch.cat([x,concat2],1)
        concat_save = self.CONCAT_FF_1(concat_save_1)+sfe_residual
        #####################################################################################################################################################################
        layer3 = self.layer3(concat_save)+concat_save #272->64
        distilled_c3, remaining_c3 = torch.split(layer3, (self.distilled_channels, self.remaining_channels), dim=1) # 16 48
        refinement_layer_3 = self.refinement_layer_3(remaining_c3)
        concat3 = torch.cat([distilled_c3,refinement_layer_3],1)
        #####################################################################################################################################################################                
        layer4 = self.layer4(torch.cat([concat_save,concat3], 1))+concat3 #336->64
        distilled_c4, remaining_c4 = torch.split(layer4, (self.distilled_channels, self.remaining_channels), dim=1) # 16 48
        refinement_layer_4 = self.refinement_layer_4(remaining_c4)
        concat4 = torch.cat([distilled_c4,refinement_layer_4],1)
        #####################################################################################################################################################################
        concat_save_2 = torch.cat([concat_save_1,concat4],1)
        concat_save = self.CONCAT_FF_2(concat_save_2)+sfe_residual
        #####################################################################################################################################################################
        x = self.CCA(concat_save)
        x = x+block_residual
        return x


class RecursiveBlock(nn.Module):
    def __init__(self,num_channels, num_features, growth_rate, num_layers, B, U,wn):
        super(RecursiveBlock, self).__init__()
        self.U = U
        
        self.G0 = num_features
        self.G = growth_rate
        self.C = num_layers
        wn = wn
        
        
        
        self.rdbs = RDB(self.G0, self.G, self.C,wn=wn) #residual dense block 생성

        
        
        
    def forward(self, sfe2):

        global test
        x=sfe2
        local_features = []
        for i in range(self.U):
            x = self.rdbs(x, sfe2)
            local_features.append(x)  #576    

        test = torch.cat(local_features, 1)
        return test
        
#High Frequency Refinement Block        
class HRB(nn.Module):
    def __init__(self, x,wn):
        super(HRB, self).__init__()
        
        self.convHRB = nn.Sequential(
                        wn(nn.Conv2d(in_channels=32,out_channels=32,kernel_size=3,padding=1,groups=1,bias=False)),
                        nn.ReLU(inplace=True),
                        wn(nn.Conv2d(in_channels=32,out_channels=32,kernel_size=3,padding=1,groups=1,bias=False)),
                        nn.ReLU(inplace=True),
                        wn(nn.Conv2d(in_channels=32,out_channels=32,kernel_size=3,padding=1,groups=1,bias=False)),
                        nn.ReLU(inplace=True),
                        wn(nn.Conv2d(in_channels=32,out_channels=32,kernel_size=3,padding=1,groups=1,bias=False)),
                        nn.ReLU(inplace=True)
                        )
        
    def forward(self, x):
        return self.convHRB(x)

class DRRDB(nn.Module):
    def __init__(self, scale_factor, num_channels, num_features, growth_rate, num_layers, B, U):
        super(DRRDB, self).__init__()
        self.scale_factor=scale_factor
        self.G0 = num_features
        self.G = growth_rate
        self.U = U
        self.C = num_layers
        self.B = B
        
        
        #Weight Normalization
        wn = lambda x: torch.nn.utils.weight_norm(x)
        self.sfe1 = wn(nn.Conv2d(num_channels, num_features, kernel_size=3, padding=3 // 2))
        self.sfe2 = wn(nn.Conv2d(num_features, num_features, kernel_size=3, padding=3 // 2))
        
        
                
        self.rbs = nn.Sequential(*[RecursiveBlock(num_channels if i==0 else num_features,
        num_features,
        growth_rate, 
        num_layers, 
        B, 
        U,wn=wn) for i in range(B)])
        
         
        
        
        
        
        
        
        
        self.HRB = HRB(num_features,wn)

        self.gff = wn(nn.Conv2d(self.G * self.U * self.B, self.G0, kernel_size=1))
            
        
        self.gff_2 = wn(nn.Conv2d(self.G0, 32, kernel_size=3, padding=3 // 2))
        
        
        # up-sampling
        assert 2 <= scale_factor <= 4
        if scale_factor == 2 or scale_factor == 4:
            self.upscale = []
            for _ in range(scale_factor // 2):
                self.upscale.extend([wn(nn.Conv2d(32, 32 * (2 ** 2), kernel_size=3, padding=3 // 2)),
                                     nn.PixelShuffle(2)])
            self.upscale = nn.Sequential(*self.upscale)
        else:
            self.upscale = nn.Sequential(
                nn.Conv2d(self.G0, self.G0 * (scale_factor ** 2), kernel_size=3, padding=3 // 2),
                nn.PixelShuffle(scale_factor)
            )

        
        self.Reconstruction = nn.Conv2d(in_channels=32,out_channels=3,kernel_size=3,padding=1,groups=1,bias=False)

    def forward(self, x):


        x_up = F.interpolate(x, mode='bicubic',scale_factor=self.scale_factor)
        sfe1 = self.sfe1(x)
        sfe2 = self.sfe2(sfe1)
        test= self.rbs(sfe2)
        
        x = self.gff(test) + sfe1
        x = self.gff_2(x)
        
        x = self.upscale(x)

        HRB_Residual=x
        x = self.HRB(x)+HRB_Residual
        
        x = self.Reconstruction(x)+x_up
        

        
        
        return x
