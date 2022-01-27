from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

button = ReplyKeyboardMarkup(
    keyboard=[

        [KeyboardButton(text='Telefonlar')],
        [KeyboardButton(text='Soatlar')],
        [KeyboardButton(text='Kompyuterl`ar')],

    ],
    resize_keyboard=True

)