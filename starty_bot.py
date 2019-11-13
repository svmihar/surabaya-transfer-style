#!/usr/bin/env python
import logging
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
        chat_id=update.effective_chat.id, text='hellow world!')


# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id,
#                              text=update.message.text)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"'{update.message.text}' ini apaan fak? gak ngerti gue")


@send_upload_photo_action
def send_photo(update, context):
    from random import choice
    pics = choice([filename for filename in Path('img').rglob('*.png')])
    print(f'sending {pics}')
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=open(pics, 'rb'))


def reply_photo(update: telegram.Update, context: telegram.Bot):
    file = context.bot.getFile(update.message.photo[-1].file_id)
    logging.info(f'file_id: {str(update.message.photo[-1].file_id)}')
    file.download('saved_image.jpg')
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('saved_image.jpg', 'rb'))


@send_upload_photo_action
def bw_photo(update, context):
    # check if photo url is valid

    from PIL import Image
    from PIL import ImageFilter
    from io import BytesIO
    from random import randint
    import os

    file = context.bot.getFile(update.message.photo[-1].file_id)
    temp_filename = f'{randint(1000,100000)}.jpg'
    logging.info(f'getting: {file}')
    file.download(temp_filename)

    image_object = Image.open(temp_filename)
    sharpened1 = image_object.filter(ImageFilter.FIND_EDGES)
    sharpened1.save(temp_filename)

    logging.info('finished')
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(temp_filename, 'rb'))
    os.system(f'rm {temp_filename}')


start_handler = CommandHandler('start', start)
photo_handler = CommandHandler('photo', send_photo)
# echo_handler = MessageHandler(Filters.text, echo)
# reply_photo_handler = MessageHandler(Filters.photo, reply_photo)
unknown_handler = MessageHandler(Filters.command, unknown)
bw_handler = MessageHandler(Filters.photo, bw_photo)
# dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
# dispatcher.add_handler(reply_photo_handler)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(bw_handler)
dispatcher.add_handler(unknown_handler)
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
