import random
import telebot
import requests
import os
from requests import Request, Session
import json
from binance import Client
import datetime

# Binance
api_key = 'hcIIyMSMHnTodQ4r30tHQZUa1sjJ6toJIlFDdFGZRD3sxwF42HNpOPIW0eoHjy8e'
api_secret = 'jZvqhOp2xr3YvcZBwPzxA5NznTT0Fh4l9iNuXcwogHSZqWS3rvZuQ9JfIV84QH7E'
client = Client(api_key, api_secret)

# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="

# Telegram
API_KEY = '5430467524:AAErQvJ-YGvSObyFWJrd_vK_pWq6QwKsU3U'
bot = telebot.TeleBot(API_KEY)

COIN_API = 'bd76f1a8-3785-4c57-8799-1f0320cb8ccd'

{
    "commands": [
        {
            "command": "Fayad"
        },
        {
            "command": "Nurlan"
        },
        {
            "command": "Azer"
        },
        {
            "command": "Obed",
            "description": "Let's have a lunch, eh?"
        },
        {
            "command": "Price"
        },
        {
            "command": "Pussy"
        }
    ],
    "language_code": "en"
}


def gst_price(coin):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': coin,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COIN_API
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    r = json.loads(response.text)['data']['GST']['quote']['USD']['price']
    b = f"GST price is: {str(round(r, 5))}"
    return b


@bot.message_handler(commands=['Nardaran'])
def gst(message):
    # current_time = now.strftime("%H:%M:%S")
    # present = datetime.datetime.now()
    # time_in_nardaran = datetime.datetime(2022, 7, 10, 12, 0, 0)
    # difference = time_in_nardaran - present
    # time_now = "Current Time = " + difference

    present = datetime.datetime.now()
    future = datetime.datetime(2022, 7, 10, 12, 0, 0)
    difference = future - present
    time_till_nardaran = "Time till Nardaran PARTYYY: " + str(difference)
    bot.send_message(message.chat.id, time_till_nardaran)


@bot.message_handler(commands=['GST'])
def gst(message):
    bot.send_message(message.chat.id, gst_price('GST'))


@bot.message_handler(commands=['Pasha'])
def find_file_ids(message):
    for file in os.listdir('audio/'):
        if file.split('.')[-1] == 'mp3':
            f = open('audio/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)


@bot.message_handler(commands=['Price'])
def prices(message):
    currencies = ["GMTUSDT", "SOLUSDT"]
    j = 0

    for i in currencies:
        url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        symb = data['symbol']
        price = data['price']
        j = j + 1
        bot.send_message(message.chat.id, f"{symb[:-4]} price is: {price[:-4]}")


@bot.message_handler(commands=['Nurlan'])
def nurlan(message):
    bot.send_message(message.chat.id, "Fuck, OPEN SHORT!")


@bot.message_handler(commands=['Prius'])
def prius(message):
    bot.send_message(message.chat.id, "Moskvada menim biznesim var, bele ozumcun sururem")


@bot.message_handler(commands=['Sakit'])
def sakit(message):
    bot.send_message(message.chat.id, "Kim sukaliyib meni?")


@bot.message_handler(commands=['Abrikos'])
def sakit(message):
    bot.send_message(message.chat.id, "Esil samogonlug maldi")


@bot.message_handler(commands=['Fayad'])
def fayad(message):
    bot.send_message(message.chat.id, "Darixmiyin, qalxacag")


@bot.message_handler(commands=['Azer'])
def azer(message):
    bot.send_message(message.chat.id, "Min shukur, brat")


@bot.message_handler(commands=['Nigar'])
def azer(message):
    bot.send_message(message.chat.id, "Bloody Mermaid huh")


@bot.message_handler(commands=['Pussy'])
def find_file_ids(message):
    for file in os.listdir('video/'):
        if file.split('.')[-1] == 'mp4':
            f = open('video/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)


@bot.message_handler(commands=['Obed'])
def obed(message):
    rand = random.randint(0, 4)
    rest = ['Mill', 'Spices', 'Nilufer', 'Salo', 'Snack']
    bot.send_message(message.chat.id, f"Let's fucking eat in {rest[rand]}")


bot.polling()

# https://api.telegram.org/5430467524:AAErQvJ-YGvSObyFWJrd_vK_pWq6QwKsU3U/getUpdates
# Group code -1001296341230
