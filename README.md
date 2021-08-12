# Recursive Distillation Super Resolution Network(RDSRN)

  * This is a repository for the network used in the master graduation paper.


![0_2page](https://user-images.githubusercontent.com/61686244/129152667-385afc5f-17dd-439b-a972-95af90b3ce85.png)

![1_2page](https://user-images.githubusercontent.com/61686244/129152680-2eacd3de-a94e-4f82-8361-9255b054a520.png)

![2_2page](https://user-images.githubusercontent.com/61686244/129152694-36082c55-c9c2-45d1-b37a-fed197393031.png)

![3_2page](https://user-images.githubusercontent.com/61686244/129152703-6b7fce12-baea-4a26-a0c6-41ba8c1adcf9.png)





 * Results of training and testing using the [Visdrone](http://aiskyeye.com/) data set

|Input(340x191)|Ground Truth(1360x764)|Bicubic Upsample(1360x764)|Super Resolution(1360x764)|
|-----|------------|----------------|----------------|
|![1_input_x4](https://user-images.githubusercontent.com/61686244/129197359-a44233f5-54dc-424c-bf63-b265b2c9cd97.png)|![100000](https://user-images.githubusercontent.com/61686244/129200210-c6452137-cb3c-4cdd-a08b-8fd88e5b44b0.png)|![1_bicubic_x4](https://user-images.githubusercontent.com/61686244/129200248-84e4bee7-1a37-4263-80fc-8539854c6698.png)|![1_SR_x4](https://user-images.githubusercontent.com/61686244/129206053-76832f7e-2fc4-4676-8971-4965dbd9d28b.png)|
|Crop Image ->|![1_crop](https://user-images.githubusercontent.com/61686244/129200401-ec4a2999-2bc3-4175-8070-d84b3d4397d2.png)|![1_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129200438-78d94715-4624-4860-a0a9-260b68c1c2af.png)|![![1_SR_x4_x4_crop](https://user-images.githubusercontent.com/61686244/129206117-e1d5939e-5794-439e-b50c-9485b9dc63cf.png)
|

|Input(350x262)|Ground Truth(1400x1048)|Bicubic Upsample(1400x1048)|Super Resolution(1400x1048)|
|-----|------------|----------------|----------------|
|![2_input_x4](https://user-images.githubusercontent.com/61686244/129201568-2390e4f8-e983-46a8-8063-501dc9337d85.png)|![101490](https://user-images.githubusercontent.com/61686244/129201499-3010f8e8-4ea0-4625-b495-a311f450a0f0.png)|![2_bicubic_x4](https://user-images.githubusercontent.com/61686244/129201611-7f7f59f3-4b9a-4a94-bb11-aea788e6b169.png)|![2_SR_x4](https://user-images.githubusercontent.com/61686244/129201718-5a7d61cb-7a6a-4c1e-a1cc-f9fb3d0c946e.png)
|Crop Image ->|![2_crop](https://user-images.githubusercontent.com/61686244/129201771-7c0e0126-ec82-407c-8f51-a8b27febc9d7.png)|![2_bicubic_x4_crop](https://user-images.githubusercontent.com/61686244/129201794-01d067be-8cd9-4af6-81b0-8c78f7e2f57f.png)|![2_SR_crop_x4](https://user-images.githubusercontent.com/61686244/129201815-9dc7f241-eb17-4983-9b10-5c07f3c8b6c7.png)|

|Input(350x197)|Ground Truth(1400x788)|Bicubic Upsample(1400x788)|Super Resolution(1400x788)|
|-----|------------|----------------|----------------|
|![5_input_x4](https://user-images.githubusercontent.com/61686244/129204018-8bb72553-94b6-4106-b7b6-1d9cca06245b.png)|![100255](https://user-images.githubusercontent.com/61686244/129203781-a692ffad-b309-4d5f-a597-ebb1b1df626e.png)|![5_bicubic_x4](https://user-images.githubusercontent.com/61686244/129204058-c98e0f7f-96fc-49e1-9eb4-fd7058d0e300.png)|![5_SR_x4](https://user-images.githubusercontent.com/61686244/129205673-50edabcf-c4d7-4f34-801f-42e21f3f94ef.png)|
|Crop Image ->|![100255_crop_x4](https://user-images.githubusercontent.com/61686244/129204143-27f42006-3656-4023-a6d2-e419254c0080.png)|![5_bicubic_x4_crop_x4](https://user-images.githubusercontent.com/61686244/129204172-84bb5cc6-9da6-4262-8bd3-aaa3ff88cf09.png)|![5_SR_x4_crop_x4](https://user-images.githubusercontent.com/61686244/129205767-d106d44e-8047-49bc-8789-7a43e3f78ad2.png)|


