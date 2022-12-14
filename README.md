# Автоматизированная загрузка фотографий космоса в Telegram-чат

Проект представляет собой набор скриптов для автоматизации сбора фотографий на космическую тематику и публикации их в Telegram-чате.

Основной скрипт запускает бота, который последовательно загружает фотографии в Telegram чат из выбранной директории, с задержкой публикации на указанное количество часов.

**Навигация по скриптам:**
***
* [Основной исполняемый скрипт](#основной-исполняемый-скрипт-main_scriptpy)
* [Скрипт для работы с Telegram-ботом](#вспомогательный-скрипт-image_botpy)
* [Скрипт для загрузки фотографий SpaceX](#вспомогательный-скрипт-fetch_spacex_imagespy)
* [Скрипт для загрузки фотографий NASA APOD](#вспомогательный-скрипт-fetch_nasa_apodpy)
* [Скрипт для загрузки фотографий NASA EPIC](#вспомогательный-скрипт-fetch_nasa_epicpy)


## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Помимо этого, для работы понадобится создать файл `.env` в корневом каталоге проекта. Данный файл необходим для работы с переменными окружения и должен содержать в себе переменные: 
```
NASA_API_KEY=<nasa_api_key>
TELEGRAM_TOKEN=<telegram_bot_token>
TELEGRAM_CHAT_ID=@<chat_id>
``` 
Для получения `NASA_API_KEY` необходимо сгенерировать ключ по ссылке [API.NASA](https://api.nasa.gov/). 

Также необходимо создать Telegram-бота, если он ещё не создан, для получения `TELEGRAM_TOKEN`. Для этого нужно обратиться к [@BotFather](https://telegram.me/BotFather). Подробная инструкция по настройке и созданию бота приведена здесь - [Инструкция по созданию Telegram-бота](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)

`TELEGRAM_CHAT_ID` - ссылка на публичный Telegram-канал (в формате `@my_chanel`), в котором будут публиковаться фотографии.

**ВАЖНО!** Бот должен быть Администратором вышеуказанного Telegram-канала.

## Использование скриптов

Проект включает в себя несколько скриптов для автоматизации разных процессов сбора и загрузки фотографий.

### Основной исполняемый скрипт `main_script.py`
Запускает бота, который последовательно загружает фотографии в Telegram-чат из выбранной директории, с задержкой публикации на указанное время. Работает в бесконечном цикле, когда фотографии для публикации заканчиваются - публикует этот же набор фотографий, но в другом порядке.
Запускается из терминала или командной строки.

Имеет два аргумента: 
* `--images_dir_path`, `-i` - путь к папке с набором фотографий. По умолчанию - 'images'
* `--sleep_time`, `-s` - время задержки публикации в часах. По умолчанию - 4 часа.

Пример запуска:
```bash
$python3 main_script.py -i pictures -s 2
```
Пример работы скрипта:

![image](https://user-images.githubusercontent.com/67222917/201514216-e2dfafd7-39d0-4f98-ba88-8ea0af009f89.png)

### Вспомогательный скрипт `image_bot.py`
Бот загружает единичную фотографию в указанный Telegram-чат. 
Запускается из терминала или командной строки.

Принимает два обязательных аргумента: 
* `--image_path`, `-i` - путь к фотографии.
* `--chat_id`, `-id` - ссылка на чат, в формате `@my_tel_ch`.

Пример запуска:
```bash
$python3 image_bot.py -i images/image_1 -id 2 @my_tel_ch.
```
Пример работы аналогичен примеру выше, за исключением того, что бот загружает по одной фотографии за запуск.

### Вспомогательный скрипт `fetch_spacex_images.py`
Через [SpaceX-API](https://github.com/r-spacex/SpaceX-API) загружает набор фотографий вылета от SpaceX по указанному ID запуска в каталог `/images`(при отсутствии создаёт его), если конкретный запуск не указан - загружает фото последнего запуска.
Запускается из терминала или командной строки.

Принимает один аргумент: 
* `--launch_id`, `-i` - ID запуска, если не указан, то скачиваются фото последнего запуска

Пример запуска:
```bash
$python3 fetch_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a
```

### Вспомогательный скрипт `fetch_nasa_apod.py`
Через [API.NASA](https://api.nasa.gov/) загружает набор фотографий на космическую тему от [NASA Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html) в каталог `/images` (при отсутствии создаёт его). Может загружать конкретное количество фотографий.
Запускается из терминала или командной строки.
Для работы требует `NASA_API_KEY` в `.env`.

Принимает один аргумент: 
* `--count`, `-c` - количество фото, которое необходимо скачать. По умолчанию - 30 шт.

Пример запуска:
```bash
$python3 fetch_nasa_apod.py --count 40
```

### Вспомогательный скрипт `fetch_nasa_epic.py`
Через [API.NASA](https://api.nasa.gov/) загружает набор фотографий земли с разных ракурсов от [NASA EPIC](https://epic.gsfc.nasa.gov/) в каталог `/images` (при отсутствии создаёт его).
Запускается из терминала или командной строки.
Для работы требует `NASA_API_KEY` в `.env`.

Пример запуска:
```bash
$python3 fetch_nasa_epic.py
```



