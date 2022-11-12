from dotenv import load_dotenv
import telegram
import os


if __name__ == '__main__':
    load_dotenv()
    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    chat_id = '@cosmo_odisey'
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    print(bot.get_me())

    bot.send_message(chat_id=chat_id, text="Hello World!")
    bot.send_photo(chat_id=chat_id, photo=open('images/epic_nasa_0.jpeg', 'rb'))

