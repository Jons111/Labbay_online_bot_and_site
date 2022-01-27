from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton


def korzinka(name):
    keys=InlineKeyboardMarkup(
        inline_keyboard=[
            [
            InlineKeyboardButton(text='Sotib olish',callback_data=f'{name}',)
        ]
        ]

    )
    return keys
