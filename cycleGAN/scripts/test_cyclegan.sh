set -ex
python test.py --dataroot ./datasets/vangogh2photo --name style_vangogh_pretrained --model test --no_dropout --preprocess scale_width --load_size 1024
