import telebot
from random import randrange

bot = telebot.TeleBot("5030747954:AAFMOqkiV6m6uKwz8n7Tta4L4pLJFU1l108")

@bot.message_handler(commands=['cocksize', 'help'])
def send_welcome(message):
	bot.reply_to(message, randrange(40))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()