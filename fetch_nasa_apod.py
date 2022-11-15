import requests
import os
from dotenv import load_dotenv
import main_loader_functions
import argparse


def fetch_nasa_apod(count, nasa_api_key):
    params = {
        'api_key' : nasa_api_key,
        'count' : count
    }
    response = requests.get(
        'https://api.nasa.gov/planetary/apod', 
        params=params
    )
    response.raise_for_status()
    for number, apod in enumerate(response.json()):
        if apod['media_type'] == 'image':
            url = apod['url']
            ext = main_loader_functions.get_extension(url)
            filename = os.path.join('images', f'nasa_apod_{number}{ext}')
            main_loader_functions.picture_loader(url, filename)
            print(f'Photo {number + 1} is load')
    print("It's done!")


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии NASA APOD. \
        Требует получения api_key, который должен быть указан в переменной .env'
    )
    parser.add_argument(
        '-c',
        '--count', 
        help='количество фото, которое необходимо скачать. По умолчанию - 30 шт.',
        default=30
    )
    args = parser.parse_args()

    fetch_nasa_apod(args.count, nasa_api_key)




    

