# surabaya on various multi style transfer learning

![](https://cdn.shopify.com/s/files/1/0627/1477/products/Starry_Night_03d43ad7-d879-40ef-8525-5f3c38918acc_grande.jpg?v=1542461422)


original image |  starry night
:-------------------------:|:-------------------------:
![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)  |  ![](img/its.png)
![](/img/../examples/inputs/surabaya.jpg)  |  ![](img/out6.png)

![](https://upload.wikimedia.org/wikipedia/commons/a/a5/Tsunami_by_hokusai_19th_century.jpg)


original image | great wave off
:-------------------------:|:-------------------------:
![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)  |  ![](img/its_wave.png)
![](/img/../examples/inputs/surabaya.jpg)  |  ![](img/surabaya_waveoff.png)


![](https://upload.wikimedia.org/wikipedia/commons/8/8d/Pierre-Auguste_Renoir_-_Luncheon_of_the_Boating_Party_-_Google_Art_Project.jpg)


original image | Luncheon of the Boating Party
:-------------------------:|:-------------------------:
![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)  |  ![](img/its_luncheon.png)
![](/img/../examples/inputs/surabaya.jpg)  |  ![](img/surabaya_luncheon.png)

![](https://upload.wikimedia.org/wikipedia/commons/5/56/Isaak_Ilitsch_Lewitan_005.jpg)


original image | levitan
:-------------------------:|:-------------------------:
![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)  |  ![](img/its_levitan.png)
![](/img/../examples/inputs/surabaya.jpg)  |  ![](img/surabaya_levitan.png)

![](https://upload.wikimedia.org/wikipedia/commons/f/ff/Camille_Pissarro_-_Boulevard_Montmartre%2C_Spring_-_Google_Art_Project.jpg)

original image | montmartre
:-------------------------:|:-------------------------:
![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)  |  ![](img/its_montmartre.png)
![](/img/../examples/inputs/surabaya.jpg)  |  ![](img/surabaya_montmartre.png)


"**insert famous painters name** painted **insert painting with different style**"
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Isaac_Levitan_-_Golden_autumn._Slobodka_-_Google_Art_Project.jpg/1600px-Isaac_Levitan_-_Golden_autumn._Slobodka_-_Google_Art_Project.jpg)
![](https://upload.wikimedia.org/wikipedia/commons/6/66/Claude_Monet_-_The_Water_Lilies_-_Setting_Sun_-_Google_Art_Project.jpg)
![](img/painting_on_painting.png)

## training
at initiation, uses a random image perception,     
using the bash script, all the pictures were trained 10 times where each layer were configured like this, gradually increasing on `image_size`, and `init_image` based on previous result:


```bash

python3 neural_style.py \
  -content_image examples/inputs/its.jpg\
  -style_image wave_off.jpg\
  -init image -init_image out5.png \
  -style_scale 1.0 \
  -print_iter 10 \
  -style_weight 2500 \
  -image_size 1024 \
  -num_iterations 2000 \
  -output_image out6.png \
  -tv_weight 0 \
  -gpu 0 \
  -backend cudnn

```


## tpu vs gpu
running on `starry_bigger_time.sh`, measured on `time_check.py`
- gpu@colab time: 3045.925956964493 s 
- gpu@p5000 time: 971.1943960189819 s 



## todo: 
- work on some styles: 
    - [ ] handwriting 
    - [ ] maps (tangerang, surabaya)
- [ ] change to celery worker
- [ ] make some quasi front end, either flask or telegram bot
    kebutuhan demo bray

## credits
- [original project based on neural algorithm of artistic style pytorch implementation](https://github.com/ProGamerGov/neural-style-pt)
- [a code based on](https://github.com/jcjohnson/neural-style)
- [original paper](http://arxiv.org/abs/1508.06576)
