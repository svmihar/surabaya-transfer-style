# surabaya on various multi style transfer learning

![](https://www.its.ac.id/wp-content/uploads/2019/07/Gambar24-1024x683.jpg)
![](https://cdn.shopify.com/s/files/1/0627/1477/products/Starry_Night_03d43ad7-d879-40ef-8525-5f3c38918acc_grande.jpg?v=1542461422)
![](img/its.png)
![](img/out6.png)
## configuration step 5
```bash

python3 neural_style.py \
  -content_image examples/inputs/surabaya.jpg\
  -style_image starry_night_gigapixel.jpg\
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