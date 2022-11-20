import argparse
import os
import random
import time

from dotenv import load_dotenv
from telegram.error import NetworkError

from image_bot import send_photo_to_chat

if __name__ == "__main__":
    load_dotenv()
    bot_token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    parser = argparse.ArgumentParser(
        description="""Бот последовательно загружает фотографии в Telegram Chat
        из выбранной директории, с задержкой публикации на указанное время.
        Бот должен быть админом чата.
        Требует TELEGRAM_TOKEN и TELEGRAM_CHAT_ID, которые должны быть указаны в переменной .env"""
    )
    parser.add_argument(
        "-i",
        "--images_dir_path",
        help="путь к директории с изображениями",
        default="images",
    )
    parser.add_argument(
        "-s",
        "--sleep_time",
        help="время задержки публикации фото, в часах",
        default=4,
        type=float,
    )
    args = parser.parse_args()
    sleep_time = args.sleep_time * 3600

    images_path_list = []
    for address, dirs, files in os.walk(args.images_dir_path):
        for name in files:
            images_path_list.append(os.path.join(address, name))

    while True:
        try:
            for image_path in images_path_list:
                send_photo_to_chat(image_path, chat_id, bot_token)
                time.sleep(sleep_time)
            random.shuffle(images_path_list)
        except NetworkError:
            print("Connection lost. Trying to reconnecting")
            time.sleep(2)
