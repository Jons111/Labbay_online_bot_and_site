from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ContentTypes, ReplyKeyboardRemove

from keyboards.default.menu import button
from states.holatlar import Forma
from loader import dp, db
from keyboards.default.tel_nomer import tel, haa, emptyy
from keyboards.default.shaxarlar import tugmalar
from keyboards.default.jins import jins
# Echo bot

@dp.message_handler(text='Tasdiqlash')
async def xabar(malumot:Message):
    await malumot.answer(text='Anketa to\'ldirish uchun ma\'lumotlaringizni kiriting',reply_markup=ReplyKeyboardRemove())
    await  malumot.answer(text='Ismni kiriting',)
    await Forma.Ism_qabul_qilish.set()
lugat = {}
@dp.message_handler(state=Forma.Ism_qabul_qilish )
async def ism_uchun(malumot:Message):
    name = malumot.text
    lugat['Ism']=name
    await  malumot.answer(text='Famni kiriting')
    await Forma.Fam_qabul_qilish.set()

@dp.message_handler(state=Forma.Fam_qabul_qilish)
async def ism_uchun(malumot:Message):
    fam = malumot.text
    lugat['Familya']=fam
    await  malumot.answer(text='Yoshni kiriting')
    await Forma.Yosh_qabul_qilish.set()

@dp.message_handler(state=Forma.Yosh_qabul_qilish )
async def ism_uchun(malumot:Message):
    yosh = malumot.text
    if not  yosh.isdigit():
        await  malumot.answer(text='Yoshni faqat raqam bilan  kiriting')
        await Forma.Yosh_qabul_qilish.set()
    else:
        lugat['Yosh']=yosh
        await  malumot.answer(text='Jins Tanlang',reply_markup=jins)
        await Forma.Jins_qabul_qilish.set()


@dp.message_handler(state=Forma.Jins_qabul_qilish )
async def ism_uchun(malumot:Message):
    kasb = malumot.text
    lugat['Jins']=kasb
    await  malumot.answer(text='Telni kiriting',reply_markup=tel)
    await Forma.Tel_qabul_qilish.set()



@dp.message_handler(state=Forma.Tel_qabul_qilish,content_types=ContentTypes.CONTACT )
async def ism_uchun(malumot:Message,state:FSMContext):
    tel = malumot.contact.phone_number
    print(tel)
    lugat['Tel']=tel
    user = malumot.from_user.username
    lugat['username']=user
    await  malumot.answer(text='shaxarni tanlang', reply_markup=tugmalar)
    await Forma.Shaxar_qabul_qilish.set()


@dp.message_handler(state=Forma.Shaxar_qabul_qilish )
async def ism_uchun(malumot:Message,state:FSMContext):
    kasb = malumot.text
    lugat['Shaxar'] = kasb
    matn = ''
    for i in lugat:
        matn += i + ':' + lugat[i] + '\n'



    await malumot.answer(text=matn, reply_markup=tugmalar)
    await malumot.answer(text='Tasdiqlang',reply_markup=haa)
    await Forma.Tasdiqlash_qabul_qilish.set()


@dp.message_handler(text='Ha',state=Forma.Tasdiqlash_qabul_qilish,)
async def ism_uchun(malumot: Message, state: FSMContext):
   print(lugat)
   ism = lugat['Ism']
   Familya = lugat['Familya']
   Yosh = lugat['Yosh']
   Jins = lugat['Jins']
   Tel= lugat['Tel']
   Shaxar = lugat['Shaxar']
   username = malumot.from_user.username
   user_id= malumot.from_user.id
   try:
        db.anketa(user_id,ism,Familya,Yosh,Tel,Jins,Shaxar,username)
   except:
       pass
   await malumot.answer(text='Tasdiqlandi !', reply_markup=button)
   await state.finish()
@dp.message_handler(state=Forma.Tasdiqlash_qabul_qilish,text="Yo'q" )
async def ism_uchun(malumot:Message,state:FSMContext):
    await malumot.answer(text='Tasdiqlanmadi !!!', reply_markup=button)
    await state.finish()