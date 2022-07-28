# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

import telebot
import random
import config
from telebot import types
# Загружаем список помещений
f = open('data/pom.txt', 'r', encoding='UTF-8')
pom = f.read()#.split('\n')
f.close()

# Создаем бота
bot = telebot.TeleBot(config.TOKEN)# Здесь мой токен, полученный от @botfather




# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):

        # Добавляем три кнопки
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Ищу свободное помещение")
        item2 = types.KeyboardButton("Контакт управляющего зданием")
        item3 = types.KeyboardButton('Перезвоните мне')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Привет, я бот 2022, помогу, чем смогу \n Нажми: \nИщу свободное помещение  \nПоказать контакт управляющего зданием \nОтправить свой контакт ',  reply_markup=markup)
# def star(message):
#     mess = f'Need help?'
#     bot.send_message(message.chat.id, mess)
@bot.message_handler(commands=["geophone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона и мы вам перезвоним! ", reply_markup=keyboard)



# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему список свободных помещений
    if message.text.strip() == 'Ищу свободное помещение' :
            # numpom = 1
            answer = pom
    # Если юзер прислал 2, выдаем контакт
    elif message.text.strip() == 'Контакт управляющего зданием':
            answer = '+375293695134 Юлия Сергеевна'
    elif message.text.strip() == 'Перезвоните мне':
            answer = geophone(message)
    else :
        answer = bot.send_message('Кнопки чуть ниже чата, выбирите из предложенных') # если не выбрали кнопку
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)

#создали перезапуск программы Menu
bot.set_my_commands([
    telebot.types.BotCommand("/start", "Перезапуск бота")

])


# Запускаем бота
bot.polling(none_stop=True, interval=0)