#!/usr/bin/env python
import logging
import time
from random import randint
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
from pathlib import Path
from functools import wraps
import json


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(
                chat_id=update.effective_message.chat_id, action=action)
            return func(update, context,  *args, **kwargs)
        return command_func

    return decorator


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
with open('secrets.json') as f:
    key = json.load(f)
updater = Updater(
    token=key[0]['api_key'], use_context=True)
dispatcher = updater.dispatcher
send_upload_photo_action = send_action(telegram.ChatAction.UPLOAD_PHOTO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='hello, please send me a pic to transfer my vangogh style to...')


@send_upload_photo_action
def bw_photo(update, context):
    # check if photo url is valid


    file = context.bot.getFile(update.message.photo[-1].file_id)
    temp_filename = f'{randint(1000,100000)}'
    logging.info(f'getting: {file}')
    os.chdir('cycleGAN/')
    dir = f'datasets/vangogh2photo/testA/'
    if not os.path.exists(dir): 
        os.makedirs(dir)
    file.download(f'{dir}/{temp_filename}.jpg')
    logging.info('mikir bentar')
    start = time.time()
    os.system('python test.py --dataroot ./datasets/vangogh2photo --name style_vangogh_pretrained --model test --no_dropout --preprocess scale_width --load_size 1024')  
    update.message.reply_text(f'took {time.time() - start} s')
    logging.info(f'took {time.time() - start} s')
    logging.info('selesai mikir')
    logging.info('sending photo now')
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(f'results/style_vangogh_pretrained/test_latest/images/{temp_filename}_fake.png', 'rb'))
    os.system(f'rm results/style_vangogh_pretrained/test_latest/images/*.png')
    os.system(f'rm datasets/vangogh2photo/testA/*.jpg')

    os.chdir('../')

@send_upload_photo_action
def linked_photo(update, context): 
    # check if photo url is valid
    link = update.message.text
    logging.info(link)
    try: 
        if link.endswith('.png') or link.endswith('.jpg'): 
            update.message.reply_text('i got your link famm, now gotta think hard.. 💆🏾')
            import requests 
            from PIL import Image
            from io import BytesIO

            os.chdir('cycleGAN/')
            temp_filename = f'{randint(1000,100000)}'
            r = requests.get(link).content
            i = Image.open(BytesIO(r))
            dir = f'datasets/vangogh2photo/testA/'
            if not os.path.exists(dir): 
                os.makedirs(dir)
            i.save(f'datasets/vangogh2photo/testA/{temp_filename}.jpg')
            start =time.time()
            os.system('python test.py --dataroot ./datasets/vangogh2photo --name style_vangogh_pretrained --model test --no_dropout --preprocess scale_width --load_size 1024')  
            update.message.reply_text(f'took {time.time() - start} s')
            logging.info(f'took {time.time() - start} s')
            logging.info('selesai mikir')
            logging.info('sending photo now')
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                   photo=open(f'results/style_vangogh_pretrained/test_latest/images/{temp_filename}_fake.png', 'rb'))
            os.system(f'rm results/style_vangogh_pretrained/test_latest/images/*.png')
            os.system(f'rm datasets/vangogh2photo/testA/*.jpg')
            os.chdir('../')
        else: 
            context.bot.send_message(chat_id=update.effecttive_chat.id, text='wrong image url')
    except Exception as e: 
        error = str(e)
        logging.info(error)
        context.bot.send_message(chat_id=update.effective_chat.id, text='are you sure the url is right?')




start_handler = CommandHandler('start', start)
bw_handler = MessageHandler(Filters.photo, bw_photo)
link_handler = MessageHandler(Filters.text, linked_photo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(link_handler)
dispatcher.add_handler(bw_handler)
logging.info('success adding now starting bot...')
logging.info('bot started')
updater.start_polling()
updater.idle()

# parameters
STYLE_IMAGE = "luncheon.jpg"
CONTENT_IMAGE = "examples/inputs/its.jpg"

STYLE_WEIGHT = 5e2
STYLE_SCALE = 1.0

STYLE_WEIGHT2 = 2500  # Style weight for image size 2048 and above
