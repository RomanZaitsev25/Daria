import telebot
from telebot import types
from config import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.InlineKeyboardButton(text="Сервис PARTNER")
    item2 = types.InlineKeyboardButton(
        text="Зарегистрироваться водителем такси")
    item3 = types.InlineKeyboardButton(text="Зарегистрироваться курьером")
    item4 = types.InlineKeyboardButton(text="ПОДДЕРЖКА")
    item5 = types.InlineKeyboardButton(text="АКЦИИ")
    item6 = types.InlineKeyboardButton(text="РОЗЫГРЫШИ")
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     'От регистрации до возможности зарабатывать 5 минут\n'
                     'Чтобы начать, нажмите\n'
                     'СТАРТ\n'
                     '👇👇👇👇👇👇👇👇\n'
                     '\n'
                     'Используйте /off чтобы приостановить подписку.\n'
                     )
    bot.send_message(message.chat.id,
                     'Хотите создать своего бота?\n'
                     'Вам сюда: @Manybot\n', reply_markup= markup
                     )


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "Сервис PARTNER":
            bot.send_message(
                message.chat.id,
                'Условия пользования\n'
                'https://telegra.ph/PARTNER-REGISTRACIYA-V-SERVISE-05-16')
        elif message.text == "Зарегистрироваться водителем такси":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.InlineKeyboardButton(text="ЛИЧНЫЕ ДАННЫЕ")
            item2 = types.InlineKeyboardButton(text="ДАННЫЕ АВТОМОБИЛЯ")
            back = types.InlineKeyboardButton(text="Назад")
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id,
                                   "Если вы хотите зарегистрироваться"
                                   "водителем такси,в нашем сервисе PARTNER,"
                                   "вам необходимо отправить боту личные "
                                   "данные и информацию о вашем автомобиле",
                             reply_markup=markup)
        elif message.text == "Зарегистрироваться курьером":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.InlineKeyboardButton(text="Курьер с автомобилем")
            item2 = types.InlineKeyboardButton(text="Курьер без автомобиля")
            back = types.InlineKeyboardButton(text="Назад")
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id,
                             "Вы хотите выполнять заказы с автомобилем "
                             "или без?",
                             reply_markup=markup)
        elif message.text == "ПОДДЕРЖКА":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
                             "Если у вас остались вопросы, можете отправить"
                             " их в ПОДДЕРЖКУ", reply_markup=markup)
        elif message.text == "АКЦИИ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
                             "Здесь будут все актуальные акции и скидки "
                             "в сервисе", reply_markup=markup)
        elif message.text == "РОЗЫГРЫШИ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
                             'Здесь будут все проходящие розыгрыши',
                             reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.InlineKeyboardButton(text="Сервис PARTNER")
            item2 = types.InlineKeyboardButton(
                text="Зарегистрироваться водителем такси")
            item3 = types.InlineKeyboardButton(
                text="Зарегистрироваться курьером")
            item4 = types.InlineKeyboardButton(text="ПОДДЕРЖКА")
            item5 = types.InlineKeyboardButton(text="АКЦИИ")
            item6 = types.InlineKeyboardButton(text="РОЗЫГРЫШИ")
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)
        elif message.text == "ЛИЧНЫЕ ДАННЫЕ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
                             'Для того чтобы зарегистрироваться водителем '
                             'такси,вам\n необходимо отправить БОТУ следующую'
                             'информацию:\n'
                             '\n'
                             'Фамилия:\n'
                             '(укажите вашу фамилию)\n'
                             'Иванов\n'
                             '\n'
                             'Имя:\n'
                             '(укажите ваше имя)\n'
                             'Иван\n'
                             '\n'
                             'Отчество:\n'
                             '(укажите отчество,если есть)\n'
                             'Иванович\n'
                             '\n'
                             'Дата рождения:\n'
                             '(укажите дату рождения)\n'
                             '01.01.2000\n'
                             '\n'
                             'Серия и номер ВУ:\n'
                             '(укажите серию и номер вашего ВУ)\n'
                             '6543 467698\n'
                             '\n'
                             'Дата выдачи ВУ:\n'
                             '(укажите дату выдачи ВУ)\n'
                             '23.11.1988\n'
                             '\n'
                             'Стаж в ВУ:\n'
                             '(укажите дату начала стажа)\n'
                             'с 12.08.1982\n'
                             '\n'
                             'Срок действия ВУ:\n'
                             '(укажите срок действия вашего ВУ)\n'
                             '12.08.1982-12.08.1992\n'
                             '\n'
                             'Страна выдачи:\n'
                             '(укажите страну получения ВУ)\n'
                             'Россия', reply_markup=markup)
        elif message.text == "ДАННЫЕ АВТОМОБИЛЯ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
                             'Данные об автомобиле:\n'
                             '\n'
                             'Серия и номер СТС:\n'
                             '(укажите серию и номер СТС)\n'
                             '\n'
                             'Модель\n'
                             'автомобиля:\n'
                             '(Укажите модель автомобиля)\n'
                             '\n'
                             'Марка автомобиля:\n'
                             '(Укажите марку автомобиля)\n'
                             '\n'
                             'Год выпуска автомобиля:\n'
                             '(Укажите год выпуска автомобиля)\n'
                             '\n'
                             'Цвет автомобиля\n:'
                             '(Укажите цвет автомобиля)\n'
                             '\n'
                             'Бренд:\n'
                             '(Укажите, если есть бренд вашего автомобиля)\n'
                             '- бренд\n'
                             '- лайтбокс\n'
                             '\n'
                             'Классификация автомобиля:\n'
                             '(Укажите класс автомобиля)\n'
                             '\n'
                             '- эконом\n'
                             '- комфорт\n'
                             '- комфорт +\n'
                             '- бизнес\n'
                             '- минивен\n', reply_markup=markup)

        elif message.text == "Курьер с автомобилем":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.InlineKeyboardButton(text="ЛИЧНЫЕ ДАННЫЕ (курьер)")
            item2 = types.InlineKeyboardButton(text="Данные автомобиля")
            back = types.InlineKeyboardButton(text="Назад")
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id,
                             "Если вы хотите зарегистрироваться курьером"
                             " на автомобиле,то\n пришлите нам данные об "
                             "автомобиле и личные данные",
                             reply_markup=markup)
        elif message.text == "Данные автомобиля":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
                             'Данные об автомобиле:\n'
                             '\n'
                             'Серия и номер СТС:\n'
                             '(укажите серию и номер СТС)\n'
                             '\n'
                             'Модель\n'
                             'автомобиля:\n'
                             '(Укажите модель автомобиля)\n'
                             '\n'
                             'Марка автомобиля:\n'
                             '(Укажите марку автомобиля)\n'
                             '\n'
                             'Год выпуска автомобиля:\n'
                             '(Укажите год выпуска автомобиля)\n'
                             '\n'
                             'Цвет автомобиля\n:'
                             '(Укажите цвет автомобиля)\n'
                             '\n'
                             'Бренд:\n'
                             '(Укажите, если есть бренд вашего автомобиля)\n'
                             '- бренд\n'
                             '- лайтбокс\n'
                             '\n'
                             'Классификация автомобиля:\n'
                             '(Укажите класс автомобиля)\n'
                             '\n'
                             '- эконом\n'
                             '- комфорт\n'
                             '- комфорт +\n'
                             '- бизнес\n'
                             '- минивен\n', reply_markup=markup)

    elif message.text == "ЛИЧНЫЕ ДАННЫЕ (курьер)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         'Данные об автомобиле:\n'
                         '\n'
                         'Серия и номер СТС:\n'
                         '(укажите серию и номер СТС)\n'
                         '\n'
                         'Модель\n'
                         'автомобиля:\n'
                         '(Укажите модель автомобиля)\n'
                         '\n'
                         'Марка автомобиля:\n'
                         '(Укажите марку автомобиля)\n'
                         '\n'
                         'Год выпуска автомобиля:\n'
                         '(Укажите год выпуска автомобиля)\n'
                         '\n'
                         'Цвет автомобиля\n:'
                         '(Укажите цвет автомобиля)\n'
                         '\n'
                         'Бренд:\n'
                         '(Укажите, если есть бренд вашего автомобиля)\n'
                         '- бренд\n'
                         '- лайтбокс\n'
                         '\n'
                         'Классификация автомобиля:\n'
                         '(Укажите класс автомобиля)\n'
                         '\n'
                         '- эконом\n'
                         '- комфорт\n'
                         '- комфорт +\n'
                         '- бизнес\n'
                         '- минивен\n', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)