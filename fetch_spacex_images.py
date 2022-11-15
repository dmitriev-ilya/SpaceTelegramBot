import requests
import os
import main_loader_functions
import argparse


def fetch_spacex_launch(launch_id): 
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    images_set = response.json()['links']['flickr']['original']
    if images_set:
        for number, image_url in enumerate(images_set):
            filename = f'images/spacex_{number}.jpeg'
            main_loader_functions.picture_loader(image_url, filename)
            print(f'Photo {number + 1} is load')
        
        print("It's done!")
    else:
        raise Exception('No images in this launch')


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии запусков SpaceX'
    )
    parser.add_argument(
        '-i',
        '--launch_id', 
        help='ID запуска, если не указан, скачиваются фото последнего запуска',
        default='latest'
    )
    args = parser.parse_args()
    
    fetch_spacex_launch(args.launch_id)



    

