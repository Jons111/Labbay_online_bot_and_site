from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Telefon'),
            KeyboardButton(text='Soat')
        ],
        [
            KeyboardButton(text='Kompyuter'),
            KeyboardButton(text='Sport')
        ],
            [
                KeyboardButton(text='Kitoblar'),
                KeyboardButton(text='Tibiyot')
            ],
        [
                 KeyboardButton(text='Savatcha')
        ],
           [
                KeyboardButton(text='Biz haqimizda ')
           ]
    ],
    resize_keyboard=True

)