import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models

from torch import Tensor
import torchvision.datasets as dset
import torchvision.transforms as T
from torchvision.transforms import Compose, Resize, ToTensor
from torch.utils.data import DataLoader
from torch.utils.data import sampler

from einops import rearrange, repeat, reduce
from einops.layers.torch import Rearrange, Reduce


class BaseModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=7, stride=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.25)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)

        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)

        x = self.conv3(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout2(x)

        x = self.avgpool(x)
        x = x.view(-1, 128)
        return self.fc(x)


############################################################################################################################################################################################
# Custom Model Template
class MyModel(nn.Module):
    def __init__(self,num_classes=18) -> None:
        super().__init__()
    
        
        self.mask_resnet18 = models.resnet18(pretrained=True)
        self.gender_resnet18 = models.resnet18(pretrained=True)
        self.under_age_resnet18 = models.resnet18(pretrained=True)
        self.over_age_resnet18 = models.resnet18(pretrained=True)
        
        self.mask_resnet18.fc = nn.Identity()
        self.gender_resnet18.fc = nn.Identity()
        self.under_age_resnet18.fc = nn.Identity()
        self.over_age_resnet18.fc = nn.Identity()
        
        for param in self.mask_resnet18.parameters():
            param.requires_grad = False

        for param in self.gender_resnet18.parameters():
            param.requires_grad = False

        for param in self.under_age_resnet18.parameters():
            param.requires_grad = False
        
        for param in self.over_age_resnet18.parameters():
            param.requires_grad = False

        self.fc_mask = nn.Linear(512, 3, bias=True)
        self.fc_gender = nn.Linear(512, 2, bias=True)
        self.fc_under_age = nn.Linear(512, 2, bias=True)
        self.fc_over_age = nn.Linear(512, 2, bias=True)

        torch.nn.init.kaiming_normal_(self.fc_mask.weight)
        torch.nn.init.kaiming_normal_(self.fc_gender.weight)
        torch.nn.init.kaiming_normal_(self.fc_under_age.weight)
        torch.nn.init.kaiming_normal_(self.fc_over_age.weight)
        
        torch.nn.init.zeros_(self.fc_mask.bias)
        torch.nn.init.zeros_(self.fc_gender.bias)
        torch.nn.init.zeros_(self.fc_under_age.bias)
        torch.nn.init.zeros_(self.fc_over_age.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        mask_x = self.mask_resnet18(x)
        gender_x= self.gender_resnet18(x)
        under_age_x=self.under_age_resnet18(x)
        over_age_x=self.over_age_resnet18(x)
        
        mask = self.fc_mask(mask_x)
        gender = self.fc_gender(gender_x)
        under_age = self.fc_under_age(under_age_x)
        over_age= self.fc_under_age(under_age_x)

        #mask_gender = torch.einsum("ij,ik->ijk", (mask, gender)).reshape(mask.shape[0], -1)
        #mask_gender_age = torch.einsum("ij,ik->ijk", (mask_gender, age)).reshape(mask_gender.shape[0], -1)

        return mask,gender,under_age,over_age   #mask_gender_age



##############################################################################################################################
class Resnet18(nn.Module):
    def __init__(self,num_classes=18) -> None:
        super().__init__()
    
        
        self.resnet18 = models.resnet18(pretrained=True)
        self.resnet18.fc = nn.Identity()
        for param in self.resnet18.parameters():
            param.requires_grad = False

        self.fc= nn.Linear(512, num_classes, bias=True)

        torch.nn.init.kaiming_normal_(self.fc.weight)
        torch.nn.init.zeros_(self.fc.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.resnet18(x)

        x = self.fc(x)

        return x 
    
class Resnet34(nn.Module):
    def __init__(self,num_classes=18) -> None:
        super().__init__()
    
        
        self.resnet34 = models.resnet34(pretrained=True)
        self.resnet34.fc = nn.Identity()
        for param in self.resnet34.parameters():
            param.requires_grad = False

        self.fc= nn.Linear(512, num_classes, bias=True)

        torch.nn.init.kaiming_normal_(self.fc.weight)
        torch.nn.init.zeros_(self.fc.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.resnet34(x)
        x = self.fc(x)

        return x 
    
class Resnet50(nn.Module):
    def __init__(self,num_classes=18) -> None:
        super().__init__()
    
        
        self.resnet50 = models.resnet50(pretrained=True)
        self.resnet50.fc = nn.Identity()
        for param in self.resnet50.parameters():
            param.requires_grad = False

        self.fc= nn.Linear(2048, num_classes, bias=True)

        torch.nn.init.kaiming_normal_(self.fc.weight)
        torch.nn.init.zeros_(self.fc.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.resnet50(x)

        x = self.fc(x)

        return x 
    
class Resnet101(nn.Module):
    def __init__(self,num_classes=18) -> None:
        super().__init__()
    
        
        self.resnet101 = models.resnet101(pretrained=True)
        self.resnet101.fc = nn.Identity()
        for param in self.resnet101.parameters():
            param.requires_grad = False

        self.fc= nn.Linear(2048, num_classes, bias=True)

        torch.nn.init.kaiming_normal_(self.fc.weight)
        torch.nn.init.zeros_(self.fc.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.resnet101(x)

        x = self.fc(x)

        return x 
 
 ##############################################################################################################################
class age_Model(nn.Module):
    def __init__(self,num_classes=2) -> None:
        super().__init__()
        num_classes=num_classes
        self.model=Resnet18(num_classes)    
        self.age_model=Resnet18(num_classes)
        
    def forward(self,x):
        age=self.model(x)
        over_age=self.age_model(x)
        return age,over_age,age+over_age
    
############################################################################################################################################################

class Teha_Resnet(nn.Module):
    def __init__(self,num_classes=3) -> None:
        super().__init__()
        num_classes=num_classes
        self.model1=Resnet18(num_classes)
        self.model2=Resnet34(num_classes)
        self.model3=Resnet50(num_classes)
        self.integrator=nn.Linear(num_classes*3,num_classes,bias=True)
        torch.nn.init.kaiming_normal_(self.integrator.weight)
        
        self.model=Resnet18(6)
    
    def forward(self,x):
        y1=self.model1(x)
        y1=torch.mul(y1,0.3*1)
        y2=self.model2(x)
        y2=torch.mul(y2,0.3*0.8)
        y3=self.model3(x)
        y3=torch.mul(y3,0.3*0.6)
        y=torch.cat((y1,y2,y3),1)
        y=self.integrator(y)
        
        z=self.model(x)
        
        return y1,y2,y3,y,z

#############################################################################################################################################################################################
class Generator(nn.Module):

    def __init__(self):
        super().__init__()

        
        self.gf=64
       
        
        self.conv1=nn.Sequential(
            nn.Conv2d(3,self.gf,4,2,1,bias=False),   # 크기 절반
            nn.LeakyReLU(0.2),
            nn.InstanceNorm2d(self.gf))
        self.conv2=nn.Sequential(
            nn.Conv2d(self.gf,self.gf*2,4,2,1,bias=False),
            nn.LeakyReLU(0.2),
            nn.InstanceNorm2d(self.gf*2))
        self.conv3=nn.Sequential(
            nn.Conv2d(self.gf*2,self.gf*4,4,2,1,bias=False),
            nn.LeakyReLU(0.2),
            nn.InstanceNorm2d(self.gf*4))
        self.conv4=nn.Sequential(
            nn.Conv2d(self.gf*4,self.gf*8,4,2,1,bias=False),
            nn.LeakyReLU(0.2),
            nn.InstanceNorm2d(self.gf*8))
        
        self.deconv1=nn.Sequential(
            nn.Upsample(scale_factor=2),          # 512 16 12
            nn.ConvTranspose2d(self.gf*8, self.gf * 4, 3, 1, 1, bias=False),   #크기 유지   256 16 12
            nn.ReLU(True),
            nn.InstanceNorm2d(self.gf*4))
        self.deconv2=nn.Sequential(
            nn.Upsample(scale_factor=2),
            nn.ConvTranspose2d(self.gf*8, self.gf * 2, 3, 1, 1, bias=False),
            nn.ReLU(True),
            nn.InstanceNorm2d(self.gf*2))
        self.deconv3=nn.Sequential(
            nn.Upsample(scale_factor=2),
            nn.ConvTranspose2d(self.gf*4, self.gf , 3, 1, 1, bias=False),
            nn.ReLU(True),
            nn.InstanceNorm2d(self.gf))
        self.ConvT=nn.ConvTranspose2d(self.gf*2, self.gf , 3, 1, 1, bias=False)
        
        self.last=nn.Sequential(
            nn.Upsample(scale_factor=2),
            nn.ConvTranspose2d(self.gf, 3 , 3, 1, 1, bias=False),
            nn.Tanh())

            
            
    
    def forward(self, x):
        # 3,128,96
        d1 = self.conv1(x)   # 64, 64, 48
        d2 = self.conv2(d1)  # 128, 32, 24
        d3 = self.conv3(d2)  # 256, 16, 12
        d4 = self.conv4(d3)  # 512, 8, 6
        
        u1 = self.deconv1(d4) # 256, 16, 12
        u1 = torch.cat([u1,d3],dim=1) #512, 16, 12 
        u2 = self.deconv2(u1) # 128, 32, 24
        u2 = torch.cat([u2,d2],dim=1) # 256, 32, 24
        u3 = self.deconv3(u2) # 64, 64, 48
        u3 = torch.cat([u3,d1], dim=1) # 128, 64, 48
        u4= self.ConvT(u3)             # 64, 64, 48
        output_img = self.last(u4)     # 64, 3, 128, 96
        
        return output_img
    
    
    
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.df=32
        
        self.d_layer1=nn.Sequential(
            nn.Conv2d(3,self.df,4,2,1,bias=False),
            nn.LeakyReLU(0.2))
        self.d_layer2=nn.Sequential(
            nn.Conv2d(self.df,self.df*2,4,2,1,bias=False),
            nn.LeakyReLU(0.2))
        self.d_layer3=nn.Sequential(
            nn.Conv2d(self.df*2,self.df*4,4,2,1,bias=False),
            nn.LeakyReLU(0.2))
        self.d_layer4=nn.Sequential(
            nn.Conv2d(self.df*4,self.df*8,4,2,1,bias=False),
            nn.LeakyReLU(0.2))
        
        self.conv=nn.Conv2d(self.df*8, 1, 3, 1, 1, bias=False)
        
        
    
    def forward(self, x):
        d1 = self.d_layer1(x)   # 32, 64, 48
        d2 = self.d_layer2(d1)  # 64, 32, 24
        d3 = self.d_layer3(d2)  # 128, 16, 12
        d4 = self.d_layer4(d3)  # 256, 8, 6

        validity = self.conv(d4)   # 1, 8, 6

        return validity
    
    
    

class ExperimentalClassifier(nn.Module):
    
    def __init__(self) -> None:
        super().__init__()

        self.fc = nn.Linear(1792, 18, bias=True)
        torch.nn.init.kaiming_normal_(self.fc.weight)
        torch.nn.init.zeros_(self.fc.bias)

        self.effnetb4 = models.efficientnet_b4(pretrained=True)
        self.effnetb4.classifier = nn.Sequential(
            nn.Dropout(p=0.4, inplace=True),
            self.fc
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.effnetb4(x)
    
    
    
    
##########################################################################################################################################################################################
class image_embedding(nn.Module):
    def __init__(self, in_channels: int = 3, img_w: int = 128, img_h: int = 96, patch_size: int = 8, emb_dim: int = 8*8*3):
        super().__init__()

        self.rearrange = Rearrange('b c (num_w p1) (num_h p2) -> b (num_w num_h) (p1 p2 c) ', p1=patch_size, p2=patch_size)
        self.linear = nn.Linear(in_channels * patch_size * patch_size, emb_dim)

        self.cls_token = nn.Parameter(torch.randn(1, 1, emb_dim))

        n_patches = img_w * img_h // patch_size**2        # N
        self.positions = nn.Parameter(torch.randn(n_patches + 1, emb_dim))

    def forward(self, x):
        batch, channel, width, height = x.shape     

        x = self.rearrange(x) # flatten patches  =>  b (c/16 * w/16) (emb_dim)
        x = self.linear(x) # embedded patches    => shape 유지

        c = repeat(self.cls_token, '() n d -> b n d', b=batch) # (self.cls_token)가 batch size 만큼 생김 (batch,1,emd_dim)
        x = torch.cat([c,x],dim=1)                             # (batch,(c/16 * w/16)+1,emb_dim)

        x = x+self.positions            #(batch,(c/16 * w/16)+1,emb_dim)
        return x
    

class multi_head_attention(nn.Module):
    def __init__(self, emb_dim: int = 8*8*3, num_heads: int = 8, dropout_ratio: float = 0.2, verbose = False, **kwargs):
        super().__init__()
        self.v = verbose

        self.emb_dim = emb_dim 
        self.num_heads = num_heads 
        self.scaling = (self.emb_dim // num_heads) ** -0.5
        
        self.value = nn.Linear(emb_dim, emb_dim)
        self.key = nn.Linear(emb_dim, emb_dim)
        self.query = nn.Linear(emb_dim, emb_dim)
        self.att_drop = nn.Dropout(dropout_ratio)

        self.linear = nn.Linear(emb_dim, emb_dim)
                
    def forward(self, x: Tensor) -> Tensor:
        # query, key, value
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)
        if self.v: print(Q.size(), K.size(), V.size()) 

        # q = k = v = patch_size**2 + 1 & h * d = emb_dim
        Q = rearrange(Q, 'b q (h d) -> b h q d', h=self.num_heads)
        K = rearrange(K, 'b k (h d) -> b h d k', h=self.num_heads)
        V = rearrange(V, 'b v (h d) -> b h v d', h=self.num_heads)
        if self.v: print(Q.size(), K.size(), V.size()) 

        ## scaled dot-product
        weight = torch.matmul(Q, K) 
        weight = weight * self.scaling
        if self.v: print(weight.size()) 
        
        attention = torch.softmax(weight, dim=-1)
        attention = self.att_drop(attention) 
        if self.v: print(attention.size())

        context = torch.matmul(attention, V) 
        context = rearrange(context, 'b h q d -> b q (h d)')
        if self.v: print(context.size())

        x = self.linear(context)
        return x , attention
    
    
class mlp_block(nn.Module):
    def __init__(self, emb_dim: int = 8*8*3, forward_dim: int = 4, dropout_ratio: float = 0.2, **kwargs):
        super().__init__()
        self.linear_1 = nn.Linear(emb_dim, forward_dim * emb_dim)
        self.dropout = nn.Dropout(dropout_ratio)
        self.linear_2 = nn.Linear(forward_dim * emb_dim, emb_dim)
        
    def forward(self, x):
        x = self.linear_1(x)
        x = nn.functional.gelu(x)
        x = self.dropout(x) 
        x = self.linear_2(x)
        return x

class encoder_block(nn.Sequential):
    def __init__(self, emb_dim:int = 8*8*3, num_heads:int = 8, forward_dim: int = 4, dropout_ratio:float = 0.2):
        super().__init__()

        self.norm_1 = nn.LayerNorm(emb_dim)
        self.mha = multi_head_attention(emb_dim, num_heads, dropout_ratio)

        self.norm_2 = nn.LayerNorm(emb_dim)
        self.mlp = mlp_block(emb_dim, forward_dim, dropout_ratio)

        self.residual_dropout = nn.Dropout(dropout_ratio)

    def forward(self, x):
        x=self.norm_1(x)                  # x = normalize (input)
        xs,attention=self.mha(x)                 # x', attention = multihead_attention (x)
        x=xs+self.residual_dropout(x)       # x = x' + residual(x)

        xs=self.norm_2(x)                   # x' = normalize(x)
        x=self.mlp(xs)                      # x' = mlp(x')
        x=xs+self.residual_dropout(x)               # x  = x' + residual(x)
        return x, attention
    
    
class vision_transformer(nn.Module):
    """ Vision Transformer model
    classifying input images (x) into classes
    """
    def __init__(self, in_channel: int = 3, img_w:int = 128, img_h:int=96,
                 patch_size: int = 8, emb_dim:int = 8*8*3, 
                 n_enc_layers:int = 15, num_heads:int = 3, 
                 forward_dim:int = 4, dropout_ratio: float = 0.2, 
                 n_classes:int = 3):
        super().__init__()

        self.in_channel=in_channel
        self.img_w=img_w
        self.img_h=img_h
        self.patch_size=patch_size
        self.emb_dim=emb_dim
        self.n_enc_layers=n_enc_layers
        self.num_heads=num_heads
        self.forward_dim=forward_dim
        self.dropout_ratio=dropout_ratio
        self.n_classes=n_classes

        # You need (1) image embedding module & (2) encoder module
        self.img_emb=image_embedding(in_channel,img_w,img_h,patch_size,emb_dim)      
        self.encoders=nn.ModuleList([encoder_block(self.emb_dim, self.num_heads,self.forward_dim,self.dropout_ratio) for _ in range(self.n_enc_layers)])

        self.reduce_layer = Reduce('b n e -> b e', reduction='mean')
        self.normalization = nn.LayerNorm(emb_dim)
        self.classification_head = nn.Linear(emb_dim, n_classes) 

    def forward(self, x):
        # (1) image embedding
        emb = self.img_emb(x)       # 1,50,16
        # (2) transformer_encoder

        attentions=[]
        for encoder in self.encoders:
            x, att = encoder(emb)
            attentions.append(att)


        x = self.reduce_layer(x)
        x = self.normalization(x)
        x = self.classification_head(x)

        return x, attentions

########################################################################################################################################################################

import torch
import torch.nn as nn
import torch.nn.functional as F
from timm.models.layers import trunc_normal_, DropPath
from timm.models.registry import register_model

class Block(nn.Module):

    def __init__(self, dim, drop_path=0., layer_scale_init_value=1e-6):
        super().__init__()
        self.dwconv = nn.Conv2d(dim, dim, kernel_size=7, padding=3, groups=dim) # depthwise conv
        self.norm = LayerNorm(dim, eps=1e-6)
        self.pwconv1 = nn.Linear(dim, 4 * dim) # pointwise/1x1 convs, implemented with linear layers
        self.act = nn.GELU()
        self.pwconv2 = nn.Linear(4 * dim, dim)
        self.gamma = nn.Parameter(layer_scale_init_value * torch.ones((dim)), 
                                    requires_grad=True) if layer_scale_init_value > 0 else None
        self.drop_path = DropPath(drop_path) if drop_path > 0. else nn.Identity()

    def forward(self, x):
        input = x
        x = self.dwconv(x)
        x = x.permute(0, 2, 3, 1)    # (N, C, H, W) -> (N, H, W, C)
        x = self.norm(x)
        x = self.pwconv1(x)
        x = self.act(x)
        x = self.pwconv2(x)
        if self.gamma is not None:
            x = self.gamma * x
        x = x.permute(0, 3, 1, 2)     # (N, H, W, C) -> (N, C, H, W)

        x = input + self.drop_path(x)
        return x

class ConvNeXt(nn.Module):

    def __init__(self, in_chans=3, num_classes=3, 
                 depths=[3, 3, 9, 3], dims=[96, 192, 384, 768], drop_path_rate=0., 
                 layer_scale_init_value=1e-6, head_init_scale=1.,
                 ):
        super().__init__()

        self.downsample_layers = nn.ModuleList() # stem and 3 intermediate downsampling conv layers
        stem = nn.Sequential(
            nn.Conv2d(in_chans, dims[0], kernel_size=4, stride=4),
            LayerNorm(dims[0], eps=1e-6, data_format="channels_first")
        )
        self.downsample_layers.append(stem)
        for i in range(3):
            downsample_layer = nn.Sequential(
                    LayerNorm(dims[i], eps=1e-6, data_format="channels_first"),
                    nn.Conv2d(dims[i], dims[i+1], kernel_size=2, stride=2),
            )
            self.downsample_layers.append(downsample_layer)

        self.stages = nn.ModuleList() # 4 feature resolution stages, each consisting of multiple residual blocks
        dp_rates=[x.item() for x in torch.linspace(0, drop_path_rate, sum(depths))] 
        cur = 0
        for i in range(4):
            stage = nn.Sequential(
                *[Block(dim=dims[i], drop_path=dp_rates[cur + j], 
                layer_scale_init_value=layer_scale_init_value) for j in range(depths[i])]
            )
            self.stages.append(stage)
            cur += depths[i]

        self.norm = nn.LayerNorm(dims[-1], eps=1e-6) # final norm layer
        self.head = nn.Linear(dims[-1], num_classes)

        self.apply(self._init_weights)
        self.head.weight.data.mul_(head_init_scale)
        self.head.bias.data.mul_(head_init_scale)

    def _init_weights(self, m):
        if isinstance(m, (nn.Conv2d, nn.Linear)):
            trunc_normal_(m.weight, std=.02)
            nn.init.constant_(m.bias, 0)

    def forward_features(self, x):
        for i in range(4):
            x = self.downsample_layers[i](x)
            x = self.stages[i](x)
        return self.norm(x.mean([-2, -1])) # global average pooling, (N, C, H, W) -> (N, C)

    def forward(self, x):
        x = self.forward_features(x)
        x = self.head(x)
        return x
    
class LayerNorm(nn.Module):
    def __init__(self, normalized_shape, eps=1e-6, data_format="channels_last"):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(normalized_shape))
        self.bias = nn.Parameter(torch.zeros(normalized_shape))
        self.eps = eps
        self.data_format = data_format
        if self.data_format not in ["channels_last", "channels_first"]:
            raise NotImplementedError 
        self.normalized_shape = (normalized_shape, )
    
    def forward(self, x):
        if self.data_format == "channels_last":
            return F.layer_norm(x, self.normalized_shape, self.weight, self.bias, self.eps)
        elif self.data_format == "channels_first":
            u = x.mean(1, keepdim=True)
            s = (x - u).pow(2).mean(1, keepdim=True)
            x = (x - u) / torch.sqrt(s + self.eps)
            x = self.weight[:, None, None] * x + self.bias[:, None, None]
            return x
########################################################################################################################################################


class BottleNeck(nn.Module):
    expansion = 4
    Cardinality = 32 # group 수
    Basewidth = 64 # bottleneck 채널이 64이면 group convolution의 채널은 depth가 됩니다.
    Depth = 4 # basewidth일 때, group convolution의 채널 수
    def __init__(self, in_channels, out_channels, stride=1):
        super().__init__()
        C = BottleNeck.Cardinality
        D = int(BottleNeck.Depth * out_channels / BottleNeck.Basewidth)

        self.conv_residual = nn.Sequential(
            nn.Conv2d(in_channels, C * D, 1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(C*D),
            nn.ReLU(),
            nn.Conv2d(C*D, C*D, 3, stride=stride, padding=1, groups=BottleNeck.Cardinality, bias=False),
            nn.BatchNorm2d(C*D),
            nn.ReLU(),
            nn.Conv2d(C*D, out_channels * BottleNeck.expansion, 1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(out_channels * BottleNeck.expansion)
        )

        self.conv_shortcut = nn.Sequential()

        if stride != 1 or in_channels != out_channels * BottleNeck.expansion:
            self.conv_shortcut = nn.Conv2d(in_channels, out_channels * BottleNeck.expansion, 1, stride=stride, padding=0)

    def forward(self, x):
        x = self.conv_residual(x) + self.conv_shortcut(x)
        return x


# ResNext
class ResNext(nn.Module):
    def __init__(self, nblocks, num_classes=3, init_weights=True):
        super().__init__()
        self.init_weights=init_weights
        self.in_channels = 64

        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, 7, stride=2, padding=2, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(3, stride=2, padding=1)
        )

        self.conv2 = self._make_res_block(nblocks[0], 64, 1)
        self.conv3 = self._make_res_block(nblocks[1], 128, 2)
        self.conv4 = self._make_res_block(nblocks[2], 256, 2)
        self.conv5 = self._make_res_block(nblocks[3], 512, 2)

        self.avg_pool = nn.AdaptiveAvgPool2d((1,1))
        self.linear = nn.Linear(512 * BottleNeck.expansion, num_classes)

        # weights initialization
        if self.init_weights:
            self._initialize_weights()

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.avg_pool(x)
        x = x.view(x.size(0), -1)
        x = self.linear(x)
        return x

    def _make_res_block(self, nblock, out_channels, stride):
        strides = [stride] + [1] * (nblock-1)
        res_block = nn.Sequential()
        for i, stride in enumerate(strides):
            res_block.add_module('dens_layer_{}'.format(i), BottleNeck(self.in_channels, out_channels, stride))
            self.in_channels = out_channels * BottleNeck.expansion
        return res_block

    # weights initialization function
    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)
        
    
########################################################################################################################################################


class ensemble(nn.Module):
    def __init__(self, num_classes =3):
        super().__init__()
        self.resnet=Teha_Resnet()
        self.vit=vision_transformer()
        self.convnext=ConvNeXt()
        self.resnext=ResNext([3, 4, 6, 3])
        self.fc=nn.Linear(num_classes*6, num_classes, bias=False)
        torch.nn.init.kaiming_normal_(self.fc.weight)
    
    def forward(self,x):
        y1,y2,y3,_=self.resnet(x)
        vit, _=self.vit(x)
        conv=self.convnext(x)
        resnext=self.resnext(x)
        y=torch.cat((y1,y2,y3,vit,conv,resnext),1)
        y=self.fc(y)
        return y1,y2,y3,vit,conv,resnext,y
        

