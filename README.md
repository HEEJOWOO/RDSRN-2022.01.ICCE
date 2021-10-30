# Recursive Distillation Super Resolution Network(RDSRN)
 [IEEE 40th International Conference on Consumer Electronics](https://www.icce.org/)
  * This is a repository for the network used in the master graduation paper.


## Network Architecture

![0_2page](https://user-images.githubusercontent.com/61686244/129152667-385afc5f-17dd-439b-a972-95af90b3ce85.png)

![1_2page](https://user-images.githubusercontent.com/61686244/129152680-2eacd3de-a94e-4f82-8361-9255b054a520.png)
 
![2_2page](https://user-images.githubusercontent.com/61686244/129152694-36082c55-c9c2-45d1-b37a-fed197393031.png)

![3_2page](https://user-images.githubusercontent.com/61686244/129152703-6b7fce12-baea-4a26-a0c6-41ba8c1adcf9.png)


  
## Train & Val
Ubuntu 18.04 LTS, Pytorch, RTX 3090 24G

The DIV2K, Set5 dataset converted to HDF5 can be downloaded from the links below.
Download Igor Pro to check h5 files.
|Dataset|Scale|Type|Link|
|-------|-----|----|----|
|DIV2K|x2|Train|[Down](https://www.dropbox.com/s/41sn4eie37hp6rh/DIV2K_x2.h5?dl=0)|
|DIV2K|x3|Train|[Down](https://www.dropbox.com/s/4piy2lvhrjb2e54/DIV2K_x3.h5?dl=0)|
|DIV2K|x4|Train|[Down](https://www.dropbox.com/s/ie4a6t7f9n5lgco/DIV2K_x4.h5?dl=0)|
|Set5|x2|Eval|[Down](https://www.dropbox.com/s/b7v5vis8duh9vwd/Set5_x2.h5?dl=0)|
|Set5|x3|Eval|[Down](https://www.dropbox.com/s/768b07ncpdfmgs6/Set5_x3.h5?dl=0)|
|Set5|x4|Eval|[Down](https://www.dropbox.com/s/rtu89xyatbb71qv/Set5_x4.h5?dl=0)|



## Quantitative comparison
 * PSNR & SSIM
  ### Set5

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Set5(PSNR,SSIM)|x2|36.66/0.9542|37.63/0.9587|37.63/0.9588|37.74/0.9597|37.78/0.9597|38.24/0.9614|38.27/0.9614|37.76/0.9590|37.90/0.9590|38.08/0.9610|

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Set5(PSNR,SSIM)|x3|32.75/0.9090|33.66/0.9213|33.82/0.9226|34.03/0.9244|34.09/0.9248|34.71/0.9296|34.74/0.9299|34.29/0.9255|-|34.42/0.9270|

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Set5(PSNR,SSIM)|x4|30.48/0.8628|31.35/0.8838|31.53/0.8854|31.68/0.8888|31.74/0.8893|32.47/0.8990|32.63/0.9002|32.13/0.8937|32.21/0.8944|32.34/0.8959|

  ### Set14

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Set14(PSNR,SSIM)|x2|32.45/0.9067|33.05/0.9127|33.06/0.9121|32.23/0.9136|33.28|0.9142|34.01/0.9212|34.12/0.9216|33.52/0.9166|33.60/0.9171|33.64/0.9181|

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Set14(PSNR,SSIM)|x3|29.29/0.8215|29.78/0.8318|29.77/0.8314|29.96/0.8349|30.00/0.8350|30.57/0.8468|30.65/0.8482|30.29/0.8407|-|30.36/0.8425|

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Set14(PSNR,SSIM)|x4|27.50/0.7513|28.02/0.7678|28.03/0.7673|28.21/0.7720|28.26/0.7723|28.81/0.7871|28.87/0.7889|28.60/0.7806|28.63/0.7813|28.72|0.7848|

  ### BSD100

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|BSD100(PSNR,SSIM)|x2|31.36/0.8435|31.90/0.8960|31.85/0.8942|32.05/0.8973|32.08/0.8978|32.34/0.9017|32.41/0.9027|32.09/0.8978|32.17/0.8989|32.33/0.9004|

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|BSD100(PSNR,SSIM)|x3|28.41/0.7863|28.83/0.7976|28.80/0.7963|28.95/0.8004|28.96/0.8001|29.26/0.8093|29.32/0.8111|29.06/0.8034|-|29.11/0.8047|
 
|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|BSD100(PSNR,SSIM)|x4|26.90/0.7103|27.29/0.7252|27.24/0.7233|27.38/0.7284|27.40/0.7281|27.72/0.7419|27.77/0.7436|27.58/0.7349|27.58/0.7356|27.66/0.7390|

  ### Urban100

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Urban100(PSNR,SSIM)|x2|29.51/0.8405|30.77/0.9141|30.76/0.9133|31.23/0.9188|31.31/0.9195|32.89/0.9353|33.34/0.9384|31.92/0.9256|32.14/0.9279|32.25/0.9294|


|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Urban100(PSNR,SSIM)|x3|26.24/0.7991|27.14/0.8279|27.15/0.8277|27.53/0.8377|27.56/0.8376|28.80/0.8653|29.09/0.8702|28.06/0.8493|-|28.08/0.8503|

|Dataset|Scale|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|-------|-----|-----|----|----|----|------|---|----|----|----|----|
|Urban100(PSNR,SSIM)|x4|24.52/0.7226|27.14/0.8279|27.15/0.8277|27.53/0.8377|27.56/0.8376|26.61/0.8028|26.82/0.8087|26.07/0.7837|26.14/0.7869|26.29/0.7918|
 
 * Params & Multi-Adds

|x4|SRCNN|VDSR|DRCN|DRRN|MemNet|RDN|RCAN|CARN|CBPN|OURS|
|--|-----|----|----|----|------|---|----|----|----|----|
|Parameter(M)|0.057|0.066|1.7|0.29|0.67|22|16|1.5|1.1|0.68|
|Multi-Adds(G)|52.7|612.6|17,974.3|6,796.9|2,662.4|1,309|919.9|90.9|97.9|136|

 * Processing Time

|Set5, x4|RDN|RCAN|CARN|OURS|
|--------|---|----|----|----|
|Processing Time(sec)|0.0172|0.066|0.0108|0.0082|


## Qualitative comparison(Video SR)
 *  Video SR result confirmation at scale factor X4 using bicubic upsample (Left) and proposed network (Right)
 *  320 x 180 to 1280 x 720


![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/61686244/129530563-294e55b3-2db1-4aea-8dfd-97ecc94dbf8f.gif)

## Qualitative comparison(Super Resolution)
 * FSR : 0.5, Recursion : 3
 * Results of testing using Urban100 data set
 * Scale Factor : x4

|Ground Truth|Bicubic|SRCNN|RDN|CARN|RDSRN|
|------------|-------|-----|---|----|-----|
|![image](https://user-images.githubusercontent.com/61686244/131208523-2b913c1a-d8ea-40f5-84c1-8cf267d3c05d.png)|![image](https://user-images.githubusercontent.com/61686244/131208528-f4ca11ef-c461-4eca-827b-5a733b8da30f.png)|![image](https://user-images.githubusercontent.com/61686244/131208531-9f838e59-adb7-4986-b692-9bc86de9f600.png)|![image](https://user-images.githubusercontent.com/61686244/131208533-dbfd69d7-3ba9-449d-91d9-a0ad7ac7432b.png)|![image](https://user-images.githubusercontent.com/61686244/131208534-bf087cd4-58fd-4983-a5cf-7cad256fefc2.png)|![image](https://user-images.githubusercontent.com/61686244/131208536-1ef2f375-51e6-4d64-becd-8cb501753ab7.png)|
|![image](https://user-images.githubusercontent.com/61686244/131208557-9e9dcc36-2117-4365-831a-2f1317be8a61.png)|![image](https://user-images.githubusercontent.com/61686244/131208559-d0089edc-afad-4d39-95cd-a6a4e856a12d.png)|![image](https://user-images.githubusercontent.com/61686244/131208560-ef5daa2d-7eda-41bf-b25b-30cd119f6942.png)|![image](https://user-images.githubusercontent.com/61686244/131208563-12900531-410f-4b4e-8af0-ba0e7f893cab.png)|![image](https://user-images.githubusercontent.com/61686244/131208565-932cc492-f517-46ed-a3ac-71b482606953.png)|![image](https://user-images.githubusercontent.com/61686244/131208568-76999655-c47b-4175-97c5-11c56b981716.png)|

|Ground Truth|Bicubic|SRCNN|RDN|CARN|RDSRN|
|------------|-------|-----|---|----|-----|
|![image](https://user-images.githubusercontent.com/61686244/131208577-a6b9c116-5363-417d-80d2-684281348214.png)|![image](https://user-images.githubusercontent.com/61686244/131208579-34691a05-d9a9-468e-bdd0-112539f34ef7.png)|![image](https://user-images.githubusercontent.com/61686244/131208583-cdc87aa6-4b8a-4acf-a232-3feefbc02e7a.png)|![image](https://user-images.githubusercontent.com/61686244/131208585-644e8513-38a5-4e7a-aea0-f8fd65b1c800.png)|![image](https://user-images.githubusercontent.com/61686244/131208588-442d05d2-9ace-4a89-bcb4-d7e885968657.png)|![image](https://user-images.githubusercontent.com/61686244/131208593-e0674d27-15eb-4fdf-afe5-cd1fad42dd3f.png)|
|![image](https://user-images.githubusercontent.com/61686244/131208595-111ee0d1-4e33-4678-88fc-345d3d712c98.png)|![image](https://user-images.githubusercontent.com/61686244/131208605-c2934ec7-4c8a-471c-b0b9-fc6d18f57220.png)|![image](https://user-images.githubusercontent.com/61686244/131208607-73cde5f3-19e2-4f50-bd42-2cdf5775560c.png)|![image](https://user-images.githubusercontent.com/61686244/131208610-4b887a39-0b81-479d-aa2e-fe8711b66a24.png)|![image](https://user-images.githubusercontent.com/61686244/131208612-e4b93452-10e1-4c55-adae-23a6b353bcf2.png)|![image](https://user-images.githubusercontent.com/61686244/131208617-7e12062a-658c-4945-8b9c-6d933fe1dd77.png)|

|Ground Truth|Bicubic|SRCNN|RDN|CARN|RDSRN|
|------------|-------|-----|---|----|-----|
|![image](https://user-images.githubusercontent.com/61686244/131208641-176f1c31-776b-4ae6-b783-ae80753e7793.png)|![image](https://user-images.githubusercontent.com/61686244/131208643-28795498-ef76-41c7-ba39-5bda38c5439b.png)|![image](https://user-images.githubusercontent.com/61686244/131208645-04d80fd6-97f8-43d3-a1a2-93b03996f78d.png)|![image](https://user-images.githubusercontent.com/61686244/131208646-52ec28c0-0266-48a0-85c2-271cacb86340.png)|![image](https://user-images.githubusercontent.com/61686244/131208649-a45fa70d-1599-4181-ba3c-5b66726b250a.png)|![image](https://user-images.githubusercontent.com/61686244/131208651-6c452415-0194-4037-ac00-15a4906af703.png)|
|![image](https://user-images.githubusercontent.com/61686244/131208654-aba498b9-3661-40aa-adcc-c1bb01cbec5d.png)|![image](https://user-images.githubusercontent.com/61686244/131208655-7a2f7546-e3bb-4104-8b79-6ba010fa06b2.png)|![image](https://user-images.githubusercontent.com/61686244/131208658-8035dc2c-e19b-464f-a8d7-90ede596cfd8.png)|![image](https://user-images.githubusercontent.com/61686244/131208660-df733c34-a35b-486a-bf92-48bbf998b139.png)|![image](https://user-images.githubusercontent.com/61686244/131208662-27973812-6c4e-46dc-b814-c0aecdf85737.png)|![image](https://user-images.githubusercontent.com/61686244/131208663-975b4567-e98e-497f-9abe-948f94b46d0a.png)|






## Qualitative comparison(Super Resolution)
 * FSR : 0.5, Recursion : 3
 * Results of training and testing using the [Visdrone](http://aiskyeye.com/) data set

|Input(340x191)|Ground Truth(1360x764)|Bicubic Upsample(1360x764)|Super Resolution(1360x764)|
|-----|------------|----------------|----------------|
|![1_input_x4](https://user-images.githubusercontent.com/61686244/129197359-a44233f5-54dc-424c-bf63-b265b2c9cd97.png)|![100000](https://user-images.githubusercontent.com/61686244/129200210-c6452137-cb3c-4cdd-a08b-8fd88e5b44b0.png)|![1_bicubic_x4](https://user-images.githubusercontent.com/61686244/129200248-84e4bee7-1a37-4263-80fc-8539854c6698.png)|![1_SR_x4](https://user-images.githubusercontent.com/61686244/129206053-76832f7e-2fc4-4676-8971-4965dbd9d28b.png)|
|Crop Image ->|![1_crop](https://user-images.githubusercontent.com/61686244/129200401-ec4a2999-2bc3-4175-8070-d84b3d4397d2.png)|![1_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129200438-78d94715-4624-4860-a0a9-260b68c1c2af.png)|![1_SR_x4_x4_crop](https://user-images.githubusercontent.com/61686244/129206117-e1d5939e-5794-439e-b50c-9485b9dc63cf.png)|

|Input(350x262)|Ground Truth(1400x1048)|Bicubic Upsample(1400x1048)|Super Resolution(1400x1048)|
|-----|------------|----------------|----------------|
|![2_input_x4](https://user-images.githubusercontent.com/61686244/129201568-2390e4f8-e983-46a8-8063-501dc9337d85.png)|![101490](https://user-images.githubusercontent.com/61686244/129201499-3010f8e8-4ea0-4625-b495-a311f450a0f0.png)|![2_bicubic_x4](https://user-images.githubusercontent.com/61686244/129201611-7f7f59f3-4b9a-4a94-bb11-aea788e6b169.png)|![2_SR_x4](https://user-images.githubusercontent.com/61686244/129201718-5a7d61cb-7a6a-4c1e-a1cc-f9fb3d0c946e.png)
|Crop Image ->|![2_crop](https://user-images.githubusercontent.com/61686244/129201771-7c0e0126-ec82-407c-8f51-a8b27febc9d7.png)|![2_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129201794-01d067be-8cd9-4af6-81b0-8c78f7e2f57f.png)|![2_SR_crop_x4](https://user-images.githubusercontent.com/61686244/129201815-9dc7f241-eb17-4983-9b10-5c07f3c8b6c7.png)|

|Input(350x197)|Ground Truth(1400x788)|Bicubic Upsample(1400x788)|Super Resolution(1400x788)|
|-----|------------|----------------|----------------|
|![5_input_x4](https://user-images.githubusercontent.com/61686244/129204018-8bb72553-94b6-4106-b7b6-1d9cca06245b.png)|![100255](https://user-images.githubusercontent.com/61686244/129203781-a692ffad-b309-4d5f-a597-ebb1b1df626e.png)|![5_bicubic_x4](https://user-images.githubusercontent.com/61686244/129204058-c98e0f7f-96fc-49e1-9eb4-fd7058d0e300.png)|![5_SR_x4](https://user-images.githubusercontent.com/61686244/129205673-50edabcf-c4d7-4f34-801f-42e21f3f94ef.png)|
|Crop Image ->|![100255_crop_x4](https://user-images.githubusercontent.com/61686244/129204143-27f42006-3656-4023-a6d2-e419254c0080.png)|![5_bicubic_x4_crop_x4](https://user-images.githubusercontent.com/61686244/129204172-84bb5cc6-9da6-4262-8bd3-aaa3ff88cf09.png)|![5_SR_x4_crop_x4](https://user-images.githubusercontent.com/61686244/129205767-d106d44e-8047-49bc-8789-7a43e3f78ad2.png)|

|Input(350x197)|Ground Truth(1400x788)|Bicubic Upsample(1400x788)|Super Resolution(1400x788)|
|-----|------------|----------------|----------------|
|![13_input_x4](https://user-images.githubusercontent.com/61686244/129206595-d3b75a79-f3a7-4e15-af54-3759518f32c5.png)|![100981](https://user-images.githubusercontent.com/61686244/129206679-cd2e70c3-86a3-4e34-831a-bd953de30ddc.png)|![13_bicubic_x4](https://user-images.githubusercontent.com/61686244/129206724-0a3bcd04-b440-4e5c-8ccc-92c5460420cb.png)|![13_SR_x4](https://user-images.githubusercontent.com/61686244/129206753-ae0eef7b-4e36-448a-a30d-df60210aa171.png)|
|Crop Image ->|![100981_crop](https://user-images.githubusercontent.com/61686244/129206804-7ceaf27b-10b9-412e-bce4-e50c702b3416.png)|![13_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129206840-bd79d73a-dfa6-4dc4-a0be-14ec48b56382.png)|![13_SR_x4_crop](https://user-images.githubusercontent.com/61686244/129206875-59fc9e09-dec2-4df1-b055-1d9b4c769cec.png)|

## Qualitative comparison(Super Resolution+denoising)
 * FSR : 0.5, Recursion : 3
 * Results of training and testing using the [Visdrone](http://aiskyeye.com/) data set
 * Replaced with crop image due to image size


|LR Input(1360x765)|Bicubic Upsample(5440x3060)|Super Resolution(5440x3060)|
|---------------|---------------------------|---------------------------|
|![input_LR_crop](https://user-images.githubusercontent.com/61686244/129523899-045efb8c-f674-4c4d-a56e-d020a47d128a.png)|![1_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129523911-00d07e25-5446-453a-b476-ce19d1a0da10.png)|![1_orginal_upsample_x4_crop](https://user-images.githubusercontent.com/61686244/129523928-195f7201-981e-4c2a-9568-edf01f657a9f.png)|

|LR+noise Input(1360x765)|Bicubic Upsample(5440x3060)|Super Resolution+denoising(5440x3060)|
|---------------|---------------------------|-------------------------------------|
|![input_LR_noise_crop](https://user-images.githubusercontent.com/61686244/129523971-b5ff8a97-3874-4e06-a2dd-0f6bf0148459.png)|![3_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129523981-06d136c7-32b7-4694-be62-503d6f7c3c00.png)|![3_orginal_upsample_x4_crop](https://user-images.githubusercontent.com/61686244/129523991-d7db2951-786f-4adc-9c56-dd0344e59572.png)|

|LR+noise Input(421x128)|Super Resolution+denoising(1684x512)|
|-----------------------|------------------------------------|
|![car_number_noise_after](https://user-images.githubusercontent.com/61686244/139525257-fd8fb2d1-c43a-4ce2-b682-6b2d2388f20f.png)|![car_number_noise_after_after_reduction_noise_x4](https://user-images.githubusercontent.com/61686244/139525261-7578b0e8-1a81-4cbe-a2a7-37acd74bfce9.png)|



## [Super Resolution+denoising+Detection Result](https://github.com/HEEJOWOO/YOLOv5_Training)









