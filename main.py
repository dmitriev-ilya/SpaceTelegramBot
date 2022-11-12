import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
from os.path import splitext
import datetime


def picture_loader(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch(id): 
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    images_set = response.json()['links']['flickr']['original']
    for number, image_url in enumerate(images_set):
        filename = f'images/spacex_{number}.jpeg'
        picture_loader(image_url, filename)

def get_extension(url):
    path = urlparse(url).path
    file_path, extension = splitext(path) 
    return extension

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
            ext = get_extension(url)
            filename = f'images/nasa_apod_{number}{ext}'
            picture_loader(url, filename)

def fetch_nasa_epic(nasa_api_key):
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images',
        params={'api_key' : nasa_api_key}
    )
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        image_name = image['image']
        data = datetime.datetime.fromisoformat(image['date'])

        image_url = f'https://api.nasa.gov/EPIC/archive/natural/' + \
            f'{data.year}/{data.month}/{data.day}/' + \
            f'png/{image_name}.png?api_key={nasa_api_key}'
        
        filename = f'images/epic_nasa_{number}.jpeg'
        picture_loader(image_url, filename)


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    
    #fetch_spacex_last_launch('5eb87d47ffd86e000604b38a')
    fetch_nasa_apod(30, nasa_api_key)
    fetch_nasa_epic(nasa_api_key)

    print("It's done!")



    

