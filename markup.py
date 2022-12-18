from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup1 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Проверка кофейни')) \
    .add(KeyboardButton('Практика бариста')) \
    .add(KeyboardButton('Отмена'))

markup2 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Отмена'))

markup3 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Эспрессо')) \
    .add(KeyboardButton('Капучино')) \
    .add(KeyboardButton('Латте')) \
    .add(KeyboardButton('Назад'))

markup4 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Назад'))

markup5 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Проверка кофейни с коментариями')) \
    .add(KeyboardButton('Выставление баллов')) \
    .add(KeyboardButton('Назад'))

button1 = KeyboardButton('5')
button2 = KeyboardButton('4')
button3 = KeyboardButton('3')
button4 = KeyboardButton('0')
button5 = KeyboardButton('1')
button6 = KeyboardButton('2')

markup6 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .row(button1, button4) \
    .add(KeyboardButton('Отмена'))

markup7 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .row(button2, button4) \
    .add(KeyboardButton('Отмена'))

markup8 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .row(button3, button4) \
    .add(KeyboardButton('Отмена'))

markup9 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .row(button6, button4) \
    .add(KeyboardButton('Отмена'))

markup10 = ReplyKeyboardMarkup(resize_keyboard=True) \
    .row(button5, button4) \
    .add(KeyboardButton('Отмена'))