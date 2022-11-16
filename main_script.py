import os
import argparse
from dotenv import load_dotenv
from image_bot import send_photo_to_chat
import random
import time
import argparse
from telegram.error import NetworkError


if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    parser = argparse.ArgumentParser(
        description="""Бот последовательно загружает фотографии в Telegram Chat
        из выбранной директории, с задержкой публикации на указанное время.
        Бот должен быть админом чата.
        Требует TELEGRAM_TOKEN и TELEGRAM_CHAT_ID, которые должны быть указаны в переменной .env"""
    )
    parser.add_argument(
        '-i',
        '--images_dir_path', 
        help='путь к директории с изображениями',
        default='images'
    )
    parser.add_argument(
        '-s',
        '--sleep_time', 
        help='время задержки публикации фото, в часах',
        default=4
    )
    args = parser.parse_args()
    sleep_time = float(args.sleep_time) * 3600

    images_path_list = []
    for address, dirs, files in os.walk(args.images_dir_path):
        for name in files:
            images_path_list.append(os.path.join(address, name))

    for image_path in images_path_list:
    	send_photo_to_chat(image_path, chat_id, bot_token)
    	time.sleep(sleep_time)

    while True:
        random.shuffle(images_path_list)
        try:    
            for image_path in images_path_list:
        	    send_photo_to_chat(image_path, chat_id, bot_token)
        	    time.sleep(sleep_time)
        except NetworkError:
            print('Connection lost. Trying to reconnecting')
            time.sleep(2)
            continue