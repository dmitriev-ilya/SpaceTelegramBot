from dotenv import load_dotenv
import telegram
import os
import argparse


def send_photo_to_chat(image_path, chat_id, bot_token):
    bot = telegram.Bot(token=bot_token)
    with open(image_path, 'rb') as image:
        bot.send_photo(chat_id=chat_id, photo=image)


if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ['TELEGRAM_TOKEN']
    parser = argparse.ArgumentParser(
        description="""Бот загружает фотографии в указанный Telegram Chat.
        Бот должен быть админом чата.
        Требует получения TELEGRAM_TOKEN, который должен быть указан в переменной .env"""
    )
    parser.add_argument(
        '-i',
        '--image_path', 
        help='путь к картинке',
    )
    parser.add_argument(
    '-id',
    '--chat_id', 
    help='ссылка на чат, в формате @my_tel_ch',
    )
    args = parser.parse_args()
    
    send_photo_to_chat(args.image_path, args.chat_id, bot_token)
    

