from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.menu import button
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user.username
    await message.answer(text=f'Labbay botga hushkelibsiz{user}', reply_markup=button)

@dp.message_handler(text='Menu')
async def bot_start(message: types.Message):
    user = message.from_user.username
    await message.answer(text=f'Labbay botga hushkelibsiz{user}', reply_markup=button)