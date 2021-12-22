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
def send_weather(message):
    city = extract_arg(message.text)[0]
    url = 'https://wttr.in/{}?format=4'.format(city)
    res = requests.get(url).text
    bot.send_message(message.chat.id, res)

@bot.inline_handler(func=lambda query: True)
def query_text(query):
    if (len(query.query) == 0):
        city = "Moscow"
    else:
        city = query.query
    try:
        url = 'https://v2.wttr.in/{}?format=%t+%c+%f+%w+%p+%P'.format(city)
        data = (requests.get(url).text).split()
        # print(city, data)

        actual = data[0]
        smile = data[1]
        feelslike = data[2]
        Wind = data[3]
        Precipitation = data[4]
        Pressure = data[5]
        info_icon = "https://d279m997dpfwgl.cloudfront.net/wp/2017/12/weather_album-art-1000x1000.jpg"
        info = types.InlineQueryResultArticle(
            id='1', title="Detailed Weather",
            description="Weather in {}".format(city),
            input_message_content=types.InputTextMessageContent(
                message_text="😱Weather in {}🙄\n"
                             "{}Actual {}\n"
                             "{}Feels Like {}\n"
                             "🌬Wind: {}\n"
                             "💧Precipitation: {}\n"
                             "🧭Pressure: {}\n"
                             "".format(city, smile, actual, smile, feelslike, Wind, Precipitation, Pressure)),
            thumb_url=info_icon, thumb_width=48, thumb_height=48
        )

        vanya_icon = "https://sun9-38.userapi.com/impg/13iRq7mq70hKhhylV614IDUt-sNW46376HZOPw/cp-udSWHFO4.jpg?size=1620x2160&quality=95&sign=705b48d9a22e7bb03500eb8d07d0171f&type=album"
        vanya = types.InlineQueryResultArticle(
            id='2', title="Парни",
            description="Горячие парни в округе",
            input_message_content=types.InputTextMessageContent(
                message_text="Ершов Иван - горячий парень"),
            thumb_url=vanya_icon, thumb_width=48, thumb_height=48
        )
        bot.answer_inline_query(query.id, [info, vanya], cache_time=1)
    except Exception as e:
        print(e)

bot.infinity_polling()