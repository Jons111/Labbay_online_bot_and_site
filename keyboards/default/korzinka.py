from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
korzinka = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Tasdiqlash'),
            KeyboardButton(text='Bekor qilish')
        ],
            [
                 KeyboardButton(text='Savatcha')
            ],
        [
            KeyboardButton(text='Menu')
        ],

    ],
    resize_keyboard=True

)