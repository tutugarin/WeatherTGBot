"""
This is my implementation of stupid and useless bot
"""

# pylint: disable-msg=consider-using-f-string
# pylint: disable-msg=missing-function-docstring
# pylint: disable-msg=broad-except

import os
from random import randrange
import requests
import telebot
from telebot import types

bot = telebot.TeleBot(os.environ['token'])

@bot.message_handler(commands=['help', 'help'])
def send_help(message):
    res = "NAME\n" \
          "\t\t @FairBoobSize_bot\n" \
          "\n" \
          "SYNOPSIS\n" \
          "\t\t@FairBoobSize_bot [город]\n" \
          "\n" \
          "DESCRIPTION\n" \
          "\t\tБот имеет две основных функции:\n" \
          "\t\t\t\t1) говорить погоду в указанном городе.\n" \
          "\t\t\t\t\t\t\t\tЕсли город не указан,\n" \
          "\t\t\t\t\t\t\t\tто по умолчанию стоит Москва\n" \
          "\t\t\t\t2) искать в округе горячих парней.\n" \
          "\t\t\t\t\t\t\t\tТак получилось, что алгоритм,\n" \
          "\t\t\t\t\t\t\t\tиспользуемый в боте,\n" \
          "\t\t\t\t\t\t\t\tсчитает только своего создателя\n" \
          "\t\t\t\t\t\t\t\tдостаточно горячим.\n"
    bot.reply_to(message, res)


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


def convert_to_celsius(temp):
    if temp[-1] == 'F':
        value = int((int(temp[:-2]) - 32) * 5 / 9)
        temp = str(value) + "°C"
    return temp


def convert_to_mps(speed):
    if speed[-3:] == "mph":
        value = int(int(speed[1:-3]) / 2.237)
        speed = speed[0] + str(value) + "m/s"
        return speed

    if speed[-4:] == "km/h":
        value = int(int(speed[1:-4]) / 3.6)
        speed = speed[0] + str(value) + "m/s"
        return speed
    return speed


@bot.inline_handler(func=lambda query: True)
def query_text(query):
    if len(query.query) == 0:
        city = "Moscow, Russia"
    else:
        city = query.query
    try:
        url = 'https://v2.wttr.in/{}?format=%t+%c+%f+%w+%p+%P'.format(city)
        data = (requests.get(url).text).split()
        # print(city, data)

        info_icon = "https://d279m997dpfwgl.cloudfront.net" \
                    "/wp/2017/12/weather_album-art-1000x1000.jpg"
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
                             "".format(city, data[1], convert_to_celsius(data[0]),
                                       data[1], convert_to_celsius(data[2]),
                                       convert_to_mps(data[3]),
                                       data[4], data[5])),
            thumb_url=info_icon, thumb_width=48, thumb_height=48
        )

        vanya_icon = "https://merriam-webster.com/" \
                     "assets/mw/images/article/" \
                     "art-wap-landing-mp-lg/" \
                     "hot-take-2974-38ae3523b46f4055f2455dcdd5a1c92f@1x.jpg"
        vanya = types.InlineQueryResultArticle(
            id='2', title="Парни",
            description="Горячие парни в округе",
            input_message_content=types.InputTextMessageContent(
                message_text="Найден 1 горячий парень:\n"
                             "1) Ершов Иван - 🔥горячий парень🔥\n"
                             "😉Девочки - пишите @tutugarin\n"
                             "🤡Маличики - не пишите"),
            thumb_url=vanya_icon, thumb_width=48, thumb_height=48
        )

        help_icon = "https://english4life.ru/wp-content/uploads/2017/05/help.jpg"
        help_info = types.InlineQueryResultArticle(
            id='3', title="man(1)",
            description="General Commands Manual",
            input_message_content=types.InputTextMessageContent(
                message_text="NAME\n"
                             "\t\t @FairBoobSize_bot\n"
                             "\n"
                             "SYNOPSIS\n"
                             "\t\t@FairBoobSize_bot [город]\n"
                             "\n"
                             "DESCRIPTION\n"
                             "\t\tБот имеет две основных функции:\n"
                             "\t\t\t\t1) говорить погоду в указанном городе.\n"
                             "\t\t\t\t\t\t\t\tЕсли город не указан,\n"
                             "\t\t\t\t\t\t\t\tто по умолчанию стоит Москва\n"
                             "\t\t\t\t2) искать в округе горячих парней.\n"
                             "\t\t\t\t\t\t\t\tТак получилось, что алгоритм,\n"
                             "\t\t\t\t\t\t\t\tиспользуемый в боте,\n"
                             "\t\t\t\t\t\t\t\tсчитает только своего создателя\n"
                             "\t\t\t\t\t\t\t\tдостаточно горячим.\n"),
            thumb_url=help_icon, thumb_width=48, thumb_height=48
        )
        bot.answer_inline_query(query.id, [info, vanya, help_info], cache_time=1)
    except Exception as exception:
        print(exception)


bot.infinity_polling()
