import requests
import os
from dotenv import load_dotenv
import main_loader_functions
import datetime
import argparse


def fetch_nasa_epic(nasa_api_key):
    params = {'api_key': nasa_api_key}
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images',
        params=params
    )
    response.raise_for_status()
    for number, image in enumerate(response.json(), start=1):
        image_name = image['image']
        date = datetime.datetime.fromisoformat(image['date'])
        year = date.strftime('%Y')
        month = date.strftime('%m')
        day = date.strftime('%d')

        image_url = (
            f'https://api.nasa.gov/EPIC/archive/natural'
            f'/{year}/{month}/{day}/png/{image_name}.png'
        )
        
        filename = os.path.join('images', f'epic_nasa_{number}.jpeg')
        main_loader_functions.picture_loader(image_url, filename, params)
        print(f'Photo {number} is load')
    print("It's done!")


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии NASA EPIC. \
        Требует получения api_key, который должен быть указан в переменной .env'
    )
    parser.parse_args()
    
    fetch_nasa_epic(nasa_api_key)