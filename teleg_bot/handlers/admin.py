from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton


 
ID = None 
 
class FSMState_ad(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    
# prendiamo ID dell'aministratore
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Vuoi inserire un prodotto?", reply_markup=admin_kb.button_case_admin)
    await message.delete()
    
# da dove parte FSM 
#@dp.message_handler(comands="load", state=None)
async def cm_start_ad(message : types.Message):
    if message.from_user.id == ID:
        await FSMState_ad.photo.set()
        await message.reply('load photo')
     
# catturiamo la prima risposta della foto
#@dp.message_handler(content_types=['photo'], state=FSMState_ad.photo)
async def load_photo(message : types.Message, state: FSMContext):
    async with state.proxy() as data_ad:
        if message.from_user.id == ID:
            data_ad['photo'] = message.photo[0].file_id
        await FSMState_ad.next()
        await message.reply('Digit name of product.')
        
# testo per uscire dallo stato FSM
#@dp.message_handler(state="*", commands='Delete')
#@dp.message_hamdler(Text(equals='delete', ignore_case=True), state="*")
async def cancel_handler_ad(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Deleted.')
    
# catturiamo la seconda risposta della nome
#@dp.message_handler( state=FSMState_ad.name)
async def load_name(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_ad:
            data_ad['name'] = message.text
        await FSMState_ad.next()
        await message.reply('Digit description.')
        
# catturiamo la terza risposta della descrizione
#@dp.message_handler(state=FSMState_ad.description)
async def load_description(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_ad:
            data_ad['description'] = message.text
        await FSMState_ad.next()
        await message.reply('Digit price.')
        
# catturiamo la quarta risposta del prezzo
#@dp.message_handler(state=FSMState_ad.price)
async def load_price(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_ad:
            data_ad['price'] = float(message.text)
    
        await sqlite_db.sql_add_command(state)    
        await state.finish()
        
#@dp.callback_query_handler(lambda x: x.data_ad and x.data_ad. startwith('del '))
async def del_callback_run(callback_querry: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_querry.data.replace('del ', ''))
    await callback_querry.answer(text=f'{(callback_querry.data.replace("del ", ""))} deleted completly', show_alert=True)

#@dp.message_handler(commands='Delete')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')
            await bot.send_message(message.from_user.id,text='press to ', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Delete completltly {ret[1]}', callback_data=f'del {ret[1]}')))
            




     
    ###############################################################
# registrazione dei handlers
def register_handlers_state_ad(dp : Dispatcher):
    dp.register_message_handler(cm_start_ad, commands="Load", state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMState_ad.photo)
    dp.register_message_handler(cancel_handler_ad, state="*", commands='Delete')
    dp.register_message_handler(cancel_handler_ad, Text(equals='delete', ignore_case=True), state="*")
    dp.register_message_handler(load_name, state=FSMState_ad.name)
    dp.register_message_handler(load_description, state=FSMState_ad.description)
    dp.register_message_handler(load_price, state=FSMState_ad.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_item, commands='Delete_product')
    
    
     