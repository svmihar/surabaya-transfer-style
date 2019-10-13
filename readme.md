# surabaya on various multi style transfer learning

![](https://cdn.shopify.com/s/files/1/0627/1477/products/Starry_Night_03d43ad7-d879-40ef-8525-5f3c38918acc_grande.jpg?v=1542461422)

original image |  starry night
:-------------------------:|:-------------------------:
![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)  |  ![](img/its.png)
![](/img/../examples/inputs/surabaya.jpg)  |  ![](img/out6.png)

![](https://upload.wikimedia.org/wikipedia/commons/a/a5/Tsunami_by_hokusai_19th_century.jpg)


original image | greate wave off
:-------------------------:|:-------------------------:
![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)  |  ![](img/its_wave.png)
![](/img/../examples/inputs/surabaya.jpg)  |  ![]()


![](https://upload.wikimedia.org/wikipedia/commons/8/8d/Pierre-Auguste_Renoir_-_Luncheon_of_the_Boating_Party_-_Google_Art_Project.jpg)
original image | greate wave off
:-------------------------:|:-------------------------:
![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)  |  ![](img/its_luncheon.png)
![](/img/../examples/inputs/surabaya.jpg)  |  ![]()
## training
using the bash script, all the pictures were trained 5 times on a configuration such as this:
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

## credits
- [original project based on neural algorithm of artistic style pytorch implementation](https://github.com/ProGamerGov/neural-style-pt)
- [a code based on](https://github.com/jcjohnson/neural-style)
- [original paper](http://arxiv.org/abs/1508.06576)