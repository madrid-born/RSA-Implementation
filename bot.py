import telebot
from telebot import types

API_KEY = '5573421122:AAG3fCZHMZr41A_jxpyGo4qgpX2bMNbnlog'
bot = telebot.TeleBot(API_KEY)
MB = 315703198


@bot.message_handler(commands=['start'])
def start_command(message):
    main_buttons(message, 'welcome to crypto bot\nwhat can i do?')


@bot.message_handler(regexp='send a message 📫')
def SM(message):
    encrypt(message)


@bot.message_handler(regexp='check the message verification ✅')
def MVC(message):
    encrypt(message)


@bot.message_handler(regexp='check the key verification ✅')
def KVC(message):
    encrypt(message)


@bot.callback_query_handler(func=lambda call: True)
def callback(query):
    flag = True
    if query.data == 'back_days':
        delete(query)
        flag = False


# bot essential

def main_buttons(message, text):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton('send a message 📫')
    button2 = types.KeyboardButton('check the message verification ✅')
    button3 = types.KeyboardButton('check the key verification ✅')
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    bot.send_message(message.chat.id, text, reply_markup=markup)


def delete(query):
    bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)


def admin(message):
    if message.chat.id == MB:
        path = ['week.xlsx', 'student.xlsx', 'mentor.xlsx', 'week(bu).xlsx', 'student(bu).xlsx', 'mentor(bu).xlsx']
        for file in path:
            with open(file, 'rb') as new_file:
                bot.send_document(message.chat.id, new_file)
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(telebot.types.InlineKeyboardButton("change files", callback_data='change'))
        keyboard.row(telebot.types.InlineKeyboardButton("talk to all users", callback_data='talk'))
        keyboard.row(telebot.types.InlineKeyboardButton("دستم خورد :)", callback_data='false alarm'))
        bot.send_message(message.chat.id, "what you wanna do?", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "you are not admin")


#

def encrypt(arg):
    pass
