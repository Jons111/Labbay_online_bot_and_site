from aiogram import types
from aiogram.dispatcher.webhook import EditMessageText
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from loader import dp, db
from keyboards.default.korzinka import korzinka
from keyboards.default.menu import button
# Echo bot
@dp.message_handler(text='Savatcha')
async def bot_echo(message: types.Message):
    username = message.from_user.username
    maxs = db.select_sold_product(username=username)

    for i in maxs:
        if int(i[3]) == 0:
            db.delete_sold_product(username=username,nomi=i[1])
        else:
            matn = f'Nomi : {i[1]} \n' \
                   f'Narxi:  {i[2]} \n' \
                   f'Miqdori: {i[3]} \n '

            key = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text='+', callback_data=f'add:{i[1]}', ),
                        InlineKeyboardButton(text='-', callback_data=f'sub:{i[1]}')
                    ]
                ]
            )
            await message.answer(text=matn, reply_markup=key)
    await message.answer(text='Sotib olish uchun tasdiqlash tugmasin bosing ',reply_markup=korzinka )



types = db.select_all_products()

royxat = []
for i in types:
    royxat.append(i[1])
for typee in royxat:
    print(typee)


    @dp.callback_query_handler(text=f'add:{typee}')
    async def bot_echo(message: CallbackQuery, ):
        username = message.from_user.username
        userid = message.from_user.id
        maxsulot_id = message.message.message_id
        print(maxsulot_id)
        maxsulot = message.data
        print(maxsulot[4:])
        maxs = db.select_sold_product(username=username, nomi=maxsulot[4:])
        for i in maxs:
            update_id = i[0]
            miqdor = i[3]
            narxi = (i[2] / miqdor) * (miqdor + 1)
            db.update_sold_product(miqdor + 1, narxi, update_id)
        username = message.from_user.username
        maxs = db.select_sold_product(username=username)


        await message.message.answer(text='changed')

for typee in royxat:
    print(typee)


    @dp.callback_query_handler(text=f'sub:{typee}')
    async def bot_echo(message: CallbackQuery, ):
        username = message.from_user.username
        userid = message.from_user.id
        maxsulot_id = message.message.message_id
        print(maxsulot_id)
        maxsulot = message.data
        print(maxsulot[4:])
        maxs = db.select_sold_product(username=username, nomi=maxsulot[4:])
        for i in maxs:
            update_id = i[0]
            miqdor = i[3]
            narxi = (i[2] / miqdor) * (miqdor -1)
            db.update_sold_product(miqdor - 1, narxi, update_id)
        username = message.from_user.username
        maxs = db.select_sold_product(username=username)


        await message.message.answer(text='changed')


@dp.message_handler(text='Bekor qilish')
async def bot_start(message: Message):
    user = message.from_user.username
    db.delete_sold_product(username=user)
    await message.answer(text=f'Bekor qilindi', reply_markup=button)