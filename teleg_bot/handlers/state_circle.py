from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text 

import gspread
from gspread import Client
import datetime
import re

def init_gspread_client():
    creds_filename = 'nome_del_tuo_file_di_credenziali.json'
    return gspread.service_account(filename=creds_filename)


class FSMState_c(StatesGroup):
    circle = State()
    step_difficult = State()
    color_quantity = State()
    production = State()
    digit_your_name = State()
    digit_your_number = State()
    
    
# da dove parte FSM 
#@dp.message_handler(text="production", state=None)
async def cm_start(query: types.CallbackQuery):
    await FSMState_c.circle.set()
    await query.message.reply('Вітаю, звідси можна почати ваш запит на отримання пропозиції для круглого килимка. Будь ласка, вкажіть бажаний діаметр килимка.')
    await query.answer()
# catturiamo la prima risposta della lungezza
#@dp.message_handler(state=FSMState.circle)
async def load_circle(message : types.Message, state: FSMContext):
    async with state.proxy() as data_c:
        try:
            data_c['circle'] = float(message.text)
            await FSMState_c.next()
        except ValueError:
            await message.reply('scrivi un numero!')
            return

    await message.reply('Digit color step difficult.')
    await message.answer('oooook')

    list_photos_ = [
        types.InputMediaPhoto(types.InputFile('img/1.jpg')),
        types.InputMediaPhoto(types.InputFile('img/2.1.jpg')),
        types.InputMediaPhoto(types.InputFile('img/3.jpg')),
    ]
    await message.answer_media_group(list_photos_)
        
        
# testo per uscire dallo stato FSM
#@dp.message_handler(state="*", commands='Delete')
#@dp.message_hamdler(Text(equals='delete', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
         return
    await state.finish()
    await message.reply('Deleted.')
        
        
        
# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.color_quantity)
async def load_color_quantity(message : types.Message, state: FSMContext):
    async with state.proxy() as data_c:
        try:
            data_c['step_difficult'] = int(message.text)
            await FSMState_c.next()
        except ValueError:
            await message.reply('scrivi un numero!')
        await message.reply('Digit normal or express production.')
        await message.answer('oooook')
        

# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.step_difficult)
async def load_step_difficult(message : types.Message, state: FSMContext):
    async with state.proxy() as data_c:
        pattern = r'^[0-9]+$'
        match = re.match(pattern, message.text)
        if not match or int(message.text) <= 0:
            await message.answer('Inserisci un numero di colori valido.')
            return
        data_c['color_quantity'] = int(message.text)
        await FSMState_c.next()
        await message.reply('Digit color quantity.')
        await message.reply('Digit normal or express production.')
            
async def load_production(message : types.Message, state: FSMContext):
    async with state.proxy() as data_c:
        pattern = r'^[a-zA-Z0-9\s]*$'
        match = re.match(pattern, message.text)
        if not match:
            await message.answer('Inserisci una produzione valida.')
            return
        data_c['production'] = str(message.text)
        await FSMState_c.next()
        await message.reply('Digit your name.')
        await message.reply('Digit normal or express production.')
        
# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.digit_your_name)
async def load_digit_your_name(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        pattern = r'^[a-zA-Z]+[a-zA-Z\s]*$'
        match = re.match(pattern, message.text)
        if not match:
            await message.answer('Inserisci un nome valido.')
            return

        data['digit_your_name'] = str(message.text)
        await FSMState_c.next()
        await message.reply('scrivi il numero tel +38_________!')
        await message.reply('Digit normal or express production.')
            
# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.digit_your_number)
async def load_digit_your_number(message : types.Message, state: FSMContext):
    async with state.proxy() as data_c:
        pattern = r'^(\+38)?[0-9]{10}$'
        match = re.match(pattern, message.text)
        if not match:
            await message.answer('Inserisci un numero di telefono valido.')
            return

        try:
            data_c['digit_your_number'] = int(match.group(0))
        except ValueError:
            await message.answer('Il numero di telefono inserito non è valido.')
            return
        # scrivo i dati nel foglio di lavoro
        async def write_to_google_sheets(data_c):
            gc = init_gspread_client()
            sheet_id = "1iDhmQAPtu6GuatI4Mk0vJ_G8XWlwmPmDEo2PcpQx5hw"
            sheet = gc.open_by_key(sheet_id).sheet1
            await message.answer("Scrivo i dati nel foglio di lavoro...")
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            num_rows = sheet.row_count
            if num_rows > 1:
                prev_row = sheet.row_values(2)  # Ottieni la prima riga dei dati
                prev_number = int(prev_row[1])  # Supponiamo che il numero sia nella colonna B
                next_number = prev_number + 1
            else:
                next_number = 1
            values_to_write = [
            #["length", "width", "color_quantity", "step_difficult"],
            [current_date, next_number,data_c['circle'], data_c['color_quantity'], data_c['step_difficult'], data_c['production'], data_c['digit_your_name'], data_c['digit_your_number']]
            ]
            sheet.insert_rows(values_to_write, 2)
            await message.answer(
                        f"caro {data_c['digit_your_name']} Lei ha inserito:\n"
                        f"circle: {data_c['circle']}\n"
                        f"step_difficult: {data_c['step_difficult']}\n"
                        f"color_quantity: {data_c['color_quantity']}\n"
                        f"produzione: {data_c['production']}\n"
                    )
        await write_to_google_sheets(data_c)
        #await message.reply(str(data))   
        await state.finish()
        
        
    
    ###############################################################

# registrazione dei handlers
def register_handlers_state_circle(dp : Dispatcher):
    dp.register_callback_query_handler(cm_start, text="production", state=None)
    dp.register_message_handler(load_circle, state=FSMState_c.circle)
    dp.register_message_handler(cancel_handler, state="*", commands='Delete')
    dp.register_message_handler(cancel_handler, Text(equals='delete', ignore_case=True), state="*")
    dp.register_message_handler(load_step_difficult, state=FSMState_c.step_difficult)
    dp.register_message_handler(load_color_quantity, state=FSMState_c.color_quantity)
    dp.register_message_handler(load_production, state=FSMState_c.production)
    dp.register_message_handler(load_digit_your_name, state=FSMState_c.digit_your_name)
    dp.register_message_handler(load_digit_your_number, state=FSMState_c.digit_your_number)
