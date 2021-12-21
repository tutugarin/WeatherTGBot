from telebot import *
import requests
import re
from random import randrange

bot = telebot.TeleBot("5030747954:AAFMOqkiV6m6uKwz8n7Tta4L4pLJFU1l108")

@bot.message_handler(commands=['cocksize', 'help'])
def send_cock(message):
    bot.reply_to(message, randrange(40))

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['weather', 'help'])
def send_welcome(message):
    city = extract_arg(message.text)[0]
    url = 'https://wttr.in/{}?format=2'.format(city)
    res = requests.get(url).text
    bot.send_message(message.chat.id, res)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        city = query.query
        url = 'https://wttr.in/{}?format=3'.format(city)
        res = requests.get(url).text
        weather_icon = "https://d279m997dpfwgl.cloudfront.net/wp/2017/12/weather_album-art-1000x1000.jpg"
        weather = types.InlineQueryResultArticle(
            id='1', title="Погода",
            description="Погода в городе: {}".format(city),
            input_message_content=types.InputTextMessageContent(
                message_text="{}".format(res)),
            thumb_url=weather_icon, thumb_width=48, thumb_height=48
        )
        bot.answer_inline_query(query.id, [weather])
    except Exception as e:
        print(e)

bot.infinity_polling()