# Recursive Distillation Super Resolution Network(RDSRN)

  * This is a repository for the network used in the master graduation paper.






## Quantitative comparison
 * PSNR & SSIM

![image](https://user-images.githubusercontent.com/61686244/129210102-c84ec6f5-2469-4b8b-a571-bc039bb6727b.png)
 
 * Params & Multi-Adds

![image](https://user-images.githubusercontent.com/61686244/129209904-4d76255a-a2ec-4b34-8bd9-9ac20335d1fe.png)

 * Processing Time

![image](https://user-images.githubusercontent.com/61686244/129210191-c1fe199b-efbc-465b-9e96-c32f706c6220.png)

## Network Architecture

![0_2page](https://user-images.githubusercontent.com/61686244/129152667-385afc5f-17dd-439b-a972-95af90b3ce85.png)

![1_2page](https://user-images.githubusercontent.com/61686244/129152680-2eacd3de-a94e-4f82-8361-9255b054a520.png)

![2_2page](https://user-images.githubusercontent.com/61686244/129152694-36082c55-c9c2-45d1-b37a-fed197393031.png)

![3_2page](https://user-images.githubusercontent.com/61686244/129152703-6b7fce12-baea-4a26-a0c6-41ba8c1adcf9.png)





## Qualitative comparison(Super Resolution)
 * FSR : 0.5, Recursion : 3
 * Results of training and testing using the [Visdrone](http://aiskyeye.com/) data set

|Input(340x191)|Ground Truth(1360x764)|Bicubic Upsample(1360x764)|Super Resolution(1360x764)|
|-----|------------|----------------|----------------|
|![1_input_x4](https://user-images.githubusercontent.com/61686244/129197359-a44233f5-54dc-424c-bf63-b265b2c9cd97.png)|![100000](https://user-images.githubusercontent.com/61686244/129200210-c6452137-cb3c-4cdd-a08b-8fd88e5b44b0.png)|![1_bicubic_x4](https://user-images.githubusercontent.com/61686244/129200248-84e4bee7-1a37-4263-80fc-8539854c6698.png)|![1_SR_x4](https://user-images.githubusercontent.com/61686244/129206053-76832f7e-2fc4-4676-8971-4965dbd9d28b.png)|
|Crop Image ->|![1_crop](https://user-images.githubusercontent.com/61686244/129200401-ec4a2999-2bc3-4175-8070-d84b3d4397d2.png)|![1_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129200438-78d94715-4624-4860-a0a9-260b68c1c2af.png)|![![1_SR_x4_x4_crop](https://user-images.githubusercontent.com/61686244/129206117-e1d5939e-5794-439e-b50c-9485b9dc63cf.png)|

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

## Qualitative comparison(Denoising + Super Resolution)
 * FSR : 0.5, Recursion : 3
 * Results of training and testing using the [Visdrone](http://aiskyeye.com/) data set

|Input(340x191)|Ground Truth(1360x764)|Bicubic Upsample(1360x764)|Super Resolution(1360x764)|
|-----|------------|----------------|----------------|
|![3_input_x4](https://user-images.githubusercontent.com/61686244/129305233-7983124a-4e07-47d3-a8db-4f806e45342b.png)|![100000](https://user-images.githubusercontent.com/61686244/129200210-c6452137-cb3c-4cdd-a08b-8fd88e5b44b0.png)|![3_bicubic_x4](https://user-images.githubusercontent.com/61686244/129305391-824e315f-2bed-4a42-a3fb-0f8fb90de74b.png)|![3_SR_x4](https://user-images.githubusercontent.com/61686244/129305420-ce70a638-d1fa-434a-96a1-7b1347307b5f.png)|
|Crop Image ->|![1_crop](https://user-images.githubusercontent.com/61686244/129200401-ec4a2999-2bc3-4175-8070-d84b3d4397d2.png)|![3_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129305624-aa0084b5-9e22-404c-907a-d143df7205cf.png)|![3_SR_x4_crop](https://user-images.githubusercontent.com/61686244/129305648-8decaef3-d86a-4291-b50a-f314017b8baf.png)|

|Input(350x262)|Ground Truth(1400x1048)|Bicubic Upsample(1400x1048)|Super Resolution(1400x1048)|
|-----|------------|----------------|----------------|
|![4_input_x4](https://user-images.githubusercontent.com/61686244/129307868-261a58d1-4b1f-48ec-a99f-62f2302be9ad.png)|![101490](https://user-images.githubusercontent.com/61686244/129201499-3010f8e8-4ea0-4625-b495-a311f450a0f0.png)|![4_bicubic_x4](https://user-images.githubusercontent.com/61686244/129307914-131ce5f0-6b2f-4d14-9786-4b0c3c6147e3.png)|![4_SR_x4](https://user-images.githubusercontent.com/61686244/129307950-d9a9f0b9-c802-4887-8dbd-1a9cfb892aff.png)
|Crop Image ->|![2_crop](https://user-images.githubusercontent.com/61686244/129201771-7c0e0126-ec82-407c-8f51-a8b27febc9d7.png)|![4_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129308112-54eaeb3e-bc8b-414f-92ad-3b4d45f8b82a.png)|![4_SR_x4_crop](https://user-images.githubusercontent.com/61686244/129308133-a1d526ac-b976-4730-b905-00b0ceb86c1f.png)|

|Input(350x197)|Ground Truth(1400x788)|Bicubic Upsample(1400x788)|Super Resolution(1400x788)|
|-----|------------|----------------|----------------|
|![2_input_x4](https://user-images.githubusercontent.com/61686244/129305783-d8a8bf1c-ca43-45f7-8671-ae05aebe0643.png)|![100255](https://user-images.githubusercontent.com/61686244/129203781-a692ffad-b309-4d5f-a597-ebb1b1df626e.png)|![2_bicubic_x4](https://user-images.githubusercontent.com/61686244/129305809-c914f1df-1dd4-4e35-a652-74598fca0380.png)|![2_SR_x4](https://user-images.githubusercontent.com/61686244/129305843-c7694dcd-ed51-4941-89fd-697d57891a70.png)|
|Crop Image ->|![100255_crop_x4](https://user-images.githubusercontent.com/61686244/129204143-27f42006-3656-4023-a6d2-e419254c0080.png)|![2_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129305981-dd796260-a2ff-4100-9288-d9b9490863cc.png)|![2_SR_x4_crop](https://user-images.githubusercontent.com/61686244/129306055-f3a904b1-f2aa-489f-9ee9-6d412489ec65.png)|

|Input(350x197)|Ground Truth(1400x788)|Bicubic Upsample(1400x788)|Super Resolution(1400x788)|
|-----|------------|----------------|----------------|
|![1_input_x4](https://user-images.githubusercontent.com/61686244/129306179-0d6a0949-2a9b-4ebe-bbeb-31c4c6e8ac76.png)|![100981](https://user-images.githubusercontent.com/61686244/129206679-cd2e70c3-86a3-4e34-831a-bd953de30ddc.png)|![1_bicubic_x4](https://user-images.githubusercontent.com/61686244/129306230-5f409efc-bfe9-4fbd-a1d7-d291434a41dc.png)|![1_SR_x4](https://user-images.githubusercontent.com/61686244/129306257-2fad2a22-28e6-422b-abd3-602887df20fc.png)|
|Crop Image ->|![100981_crop](https://user-images.githubusercontent.com/61686244/129206804-7ceaf27b-10b9-412e-bce4-e50c702b3416.png)||![1_SR_x4_crop](https://user-images.githubusercontent.com/61686244/129306416-56eaea7c-721f-4007-913d-a1f431b2f613.png)|

