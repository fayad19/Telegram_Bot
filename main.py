import random
import telebot
import requests
import os
from requests import Request, Session
import json
from binance import Client
import datetime
from datetime import datetime

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

    present = datetime.now()
    future = datetime(2022, 9, 18, 13, 0, 0)
    difference = future - present
    if present < future:
        time_till_nardaran = "Don't miss! Time till Last Pool Party of the year: " + str(difference)
    else:
        time_till_nardaran = "Siz Landmarki sevmiyorsunuz, ne parti ya"
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

    curr_time = datetime.now()
    curr_time_str = curr_time.strftime("%m-%d-%Y, %H:%M:%S")

    with open('gst_price.json', 'r') as openfile:
        # Reading from json file
        coin_prices = json.load(openfile)

    last_check_time = datetime.strptime(coin_prices[3]['time'], "%m-%d-%Y, %H:%M:%S")

    diff = curr_time - last_check_time
    minn = round(diff.seconds // 60)

    if diff.seconds < 3600:
        if minn < 2 and minn != 0:
            bot.send_message(message.chat.id, "Price was last checked " + str(minn) + " minute ago")
        else:
            bot.send_message(message.chat.id, "Price was last checked " + str(minn) + " minutes ago")
    else:
        if minn % 60 > 1 and minn % 60 != 0:
            bot.send_message(message.chat.id, "Price was last checked " + str(round(minn / 60)) + " hours and " + str(
                minn % 60) + " minutes ago")
        else:
            bot.send_message(message.chat.id, "Price was last checked " + str(round(minn / 60)) + " hours and " + str(
                minn % 60) + " minute ago")

    dictionary = ["data:"]

    j = 0
    for i in currencies:
        url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        symb = data['symbol']
        price = data['price']
        j = j + 1
        coins = {'name': symb[:-4] for i in range(2)}
        dictionary.append(coins)
        # print(dictionary)
        prices = {'price': price[:-4] for i in range(2)}
        dictionary.append(prices)
        dictionary.append({"time": curr_time_str})
        old_gmt_price = coin_prices[2]['price']
        old_sol_price = coin_prices[5]['price']

        # Bot sending price of coins
        if symb[:-4] == "GMT" :
            if price[:-4] < coin_prices[2]['price']:
                bot.send_message(message.chat.id,
                                 f'{symb[:-4]} price is going down \u2B07: {price[:-4]}. Previous price was {old_gmt_price}')
            else:
                bot.send_message(message.chat.id,
                                 f'{symb[:-4]} price is going up \u2B06: {price[:-4]}. Previous price was {old_gmt_price}')
        elif symb[:-4] == "SOL" :
            if price[:-4] < coin_prices[5]['price']:
                bot.send_message(message.chat.id,
                                 f'{symb[:-4]} price is going down \u2B07: {price[:-4]}. Previous price was {old_sol_price}')
            else:
                bot.send_message(message.chat.id,
                                 f'{symb[:-4]} price is going up \u2B06: {price[:-4]}. Previous price was {old_sol_price}')

    with open("gst_price.json", "w") as outfile:
        json.dump(dictionary, outfile)

    gst(message)


@bot.message_handler(commands=['Nurlan'])
def nurlan(message):
    bot.send_message(message.chat.id, "Fuck, OPEN SHORT!")


@bot.message_handler(commands=['Prius'])
def prius(message):
    bot.send_message(message.chat.id, "Moskvada menim biznesim var, bele ozumcun sururem")


@bot.message_handler(commands=['Sakit'])
def sakit(message):
    bot.send_message(message.chat.id, "Kim sukaliyib meni?")


@bot.message_handler(commands=['Gravy'])
def gravy(message):
    bot.send_message(message.chat.id, "Sukaliyanlar ucun babat sous var")


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


@bot.message_handler(commands=['Traitor'])
def find_file_ids(message):
    f = open('animation/traitor.gif', 'rb')
    bot.send_animation(message.chat.id, f, None)
    f.close()


@bot.message_handler(commands=['Obed'])
def obed(message):
    rand = random.randint(0, 4)
    rest = ['Mill', 'Spices', 'Nilufer', 'Salo', 'Snack']
    bot.send_message(message.chat.id, f"Let's fucking eat in {rest[rand]}")


bot.polling()

# https://api.telegram.org/5430467524:AAErQvJ-YGvSObyFWJrd_vK_pWq6QwKsU3U/getUpdates
# Group code -1001296341230
