from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/stop')
button3 = types.KeyboardButton(text='/инфо')
button4 = types.KeyboardButton(text='покажи лису')
button5 = types.KeyboardButton(text='/prof')

keyboard1 = [
    [button1, button2, button3],
    [button4, button5],
]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)