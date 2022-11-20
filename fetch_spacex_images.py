import argparse
import os

import requests

import main_loader_functions


class EmptyImagesSetError(Exception):
    pass


def fetch_spacex_launch(launch_id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    images_set = response.json()["links"]["flickr"]["original"]
    if not images_set:
        raise EmptyImagesSetError("No images in this launch")
    for number, image_url in enumerate(images_set, start=1):
        filename = os.path.join("images", f"spacex_{number}.jpeg")
        main_loader_functions.load_picture(image_url, filename)
        print(f"Photo {number} is load")
    print("It's done!")


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    parser = argparse.ArgumentParser(
        description="Программа скачивает фотографии запусков SpaceX"
    )
    parser.add_argument(
        "-i",
        "--launch_id",
        help="ID запуска, если не указан, скачиваются фото последнего запуска",
        default="latest",
    )
    args = parser.parse_args()

    fetch_spacex_launch(args.launch_id)
