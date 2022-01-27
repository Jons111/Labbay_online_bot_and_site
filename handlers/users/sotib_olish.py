from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp,db


# Echo bot
maxsulotlar = db.select_all_products()
royxat = []
for maxx in maxsulotlar:
   royxat.append(maxx[1])

print(royxat)
for nomi in royxat:
   print(nomi)
   @dp.callback_query_handler(text=f'{nomi}')
   async def bot_echo(call:CallbackQuery, state: FSMContext ):

      nomi= (call.data)
      maxs =  db.select_product(nomi=nomi)
      narxi = maxs[2]
      nomi = maxs[1]
      turi = 2
      print(turi)
      miqdori = 1

      idlar = [0]
      username = str(call.from_user.username)
      maxs = db.select_sold_product(username=username)
      print(maxs)
      for i in maxs:
         idlar.append(i[1])

      if nomi in idlar:
         nom = db.select_sold_product(username=username, nomi=nomi)[0]
         miqdori = nom[3]
         miqdori += 1

         nomi = str(nom[1])
         maxs_id = nom[0]

         db.update_sold_product(miqdori=miqdori,narxi=narxi*miqdori,id=maxs_id,)

      else:

         idlar = [0]
         s = db.select_all_sold_product()
         for i in s:
            idlar.append(i[0])
         maxx_id = max(idlar)
         db.add_sold_product(id=maxx_id+1, nomi=nomi, narxi=narxi, miqdori=miqdori, tur=turi, username=username)



      await call.message.answer(text=f'maxsulot qabul qilindi')
