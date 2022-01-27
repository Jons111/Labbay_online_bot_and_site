from aiogram import types
from aiogram.types import InputFile, Message

from loader import dp,db,bot
from keyboards.inline.korzinka import korzinka
from aiogram.types import CallbackQuery
# Echo bot
types = db.select_all_type()
print(types)
royxat = []
for i in types:
    royxat.append(i[1])
for typee in royxat:

    @dp.message_handler(text=f'{typee}')
    async def bot_echo(message: Message):
        maxsulot = message.text
        maxs = db.select_type(nomi=maxsulot)

        user_id= message.from_user.id
        maxsulotlar = db.filter_product(tur_id=maxs[0])
        for maxs in maxsulotlar:
            nomi = maxs[1]
            narxi = maxs[2]
            tarif = maxs[3]
            rasm1 =InputFile(path_or_bytesio= maxs[4])
            await bot.send_photo(chat_id=user_id,photo=rasm1,
                    caption=f'Nomi : {nomi}\n'
                            f'Narxi : {narxi}\n'
                            f'Tarif : {tarif}\n',
                            reply_markup=korzinka(nomi))

