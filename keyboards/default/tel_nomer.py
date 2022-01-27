from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

tel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kontakt",request_contact=True,one_time_keyboard=True)
        ],

    ],
  resize_keyboard=True
)


haa = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha",)
        ],
        [
            KeyboardButton(text="Yo'q",)
        ],

    ],
  resize_keyboard=True
)

emptyy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" ",)
        ],


    ],
  resize_keyboard=True
)