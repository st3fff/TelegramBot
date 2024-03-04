import telebot
import webbrowser
from telebot import types
import sqlite3

bot = telebot.TeleBot('7077068591:AAFwlGRfcmjKv-P6tgXamj6O3gDH_Pzj8SU')
name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('stef.sql')
    cur =  conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет,давай тебя зарегистрируем! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('stef.sql')
    cur =  conn.cursor()

    cur.execute(f'INSERT INTO users(name, pass)VALUES ({name},{password})')
    conn.commit()
    cur.close()
    conn.close()
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на сайт 😃')
#     markup.row(btn1)
#     btn2 = types.KeyboardButton('Удалить фото')
#     btn3 = types.KeyboardButton('Изменить текст')
#     markup.row(btn2,btn3)
#     file = open('./photo.jpeg','rb')
#     bot.send_photo(message.chat.id, file, reply_markup=markup)
#     bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)

# def on_click(message):
#     if message.text == "Перейти на сайт 😃":
#         url = 'https://github.com/st3fff'
#         webbrowser.open(url)
#         bot.send_message(message.chat.id, f"Открыл ссылку {url}")
#     elif message.text == 'Удалить фото':
#         bot.send_message(message.chat.id, 'Deleted')
        

    

# @bot.message_handler(commands=['site','website'])
# def site(message):
#     webbrowser.open('https://github.com/st3fff')    

# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}')


# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>Help</b> <u>information</u>', parse_mode='html')

# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#          bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')

# @bot.message_handler(content_types=["photo"])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/st3fff')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     markup.row(btn2,btn3)
#     bot.reply_to(message, "Какое красивое фото! ", reply_markup=markup)


# @bot.callback_query_handler(func=lambda callback: True) 
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)




bot.polling(none_stop=True)  
