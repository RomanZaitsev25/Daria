import datetime

import requests
import telebot
from telebot import types
from config import config
from weather import get_weather
open_weather_token = '102ed5a661bc6087b45932ab7045dd47'

bot = telebot.TeleBot(config.TOKEN)


def get_rate():
    response = requests.get(
        'https://belarusbank.by/api/kursExchange?city=Несвиж'
    )
    if response.ok:
        return response.json()
    return []


@bot.message_handler(commands=['start'])
def start(message):
    # создадим обычную клавиатуру. resize_keyboard- позволять изменять размер,
    # и влазить в клавиатуру.
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(text="КУРСЫ ВАЛЮТ")
    item2 = types.KeyboardButton(text="ПРОГНОЗ ПОГОДЫ")
    item3 = types.KeyboardButton(text="ДРУГОЕ")
    # Добавляет кнопки.
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     'Чтобы начать, нажмите\n'
                     'СТАРТ\n'
                     '👇👇👇👇👇👇👇👇\n'
                     '\n'
                     )
    bot.send_message(message.chat.id,
                     'Что бы создать своего бота?\n'
                     'Перейдите вот сюда: @Manybot\n', reply_markup=markup
                     )


@bot.message_handler(content_types=['text'])
def bot_message(message):
    # не телеграмм канал а личное сообщение
    if message.chat.type == 'private':
        if message.text == "КУРСЫ ВАЛЮТ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton(text="Курс USD")
            item2 = types.KeyboardButton(text="Курс EUR")
            item3 = types.KeyboardButton(text="Курс RUB")
            item4 = types.KeyboardButton(text="Курс PLN")
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id,
                             "Здесь представлен курс различных валют в банке",
                             reply_markup=markup)
        elif message.text == "ПРОГНОЗ ПОГОДЫ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton(text="Введите город:")
            back = types.KeyboardButton('Назад')
            markup.add(item1, back)
            bot.send_message(message.chat.id,
                             "Информаци о прогонозе погоды\n"
                             "в различных городах", reply_markup=markup)
        elif message.text == "ДРУГОЕ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
                             "ЕЩЕ НЕ ПРИДУМАЛ", reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton(text="КУРСЫ ВАЛЮТ")
            item2 = types.KeyboardButton(text="ПРОГНОЗ ПОГОДЫ")
            item3 = types.KeyboardButton(text="ДРУГОЕ")
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Главное меню',
                             reply_markup=markup)

        elif message.text == 'Курс USD':
            data = get_rate()
            out_message = ''
            for info in data:
                out_message += 'Курс продажи {}, курс покупки {}.\n'.format(
                    info['USD_in'], info['USD_out']
                )
            if not out_message:
                out_message = 'Сайт сейчас не доступен.'
            bot.send_message(message.chat.id, out_message)

        elif message.text == 'Курс EUR':
            data = get_rate()
            out_message = ''
            for info in data:
                out_message += 'Курс продажи {}, курс покупки {}.\n'.format(
                    info['EUR_in'], info['EUR_out']
                )
            if not out_message:
                out_message = 'Сайт сейчас не доступен.'
            bot.send_message(message.chat.id, out_message)

        elif message.text == 'Курс RUB':
            data = get_rate()
            out_message = ''
            for info in data:
                out_message += 'Курс продажи {}, курс покупки {}.\n'.format(
                    info['RUB_in'], info['RUB_out']
                )
            if not out_message:
                out_message = 'Сайт сейчас не доступен.'
            bot.send_message(message.chat.id, out_message)

        elif message.text == 'Курс PLN':
            data = get_rate()
            out_message = ''
            for info in data:
                out_message += 'Курс продажи за 100 злотых {},\n' \
                               'Курс покупки за 100 злотых {}.\n' \
                    .format(info['PLN_in'], info['PLN_out']
                            )
            if not out_message:
                out_message = 'Сайт сейчас не доступен.'
            bot.send_message(message.chat.id, out_message)


def main():
    city = input('Введите город:')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    bot.polling(none_stop=True)
