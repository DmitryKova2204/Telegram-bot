from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Orario'), KeyboardButton(text='Aula')]
],
                resize_keyboard=True)