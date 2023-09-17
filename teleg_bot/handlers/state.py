from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text 
import re
import gspread
from gspread import Client
import datetime

def init_gspread_client():
    creds_filename = 'nome_del_tuo_file_di_credenziali.json'
    return gspread.service_account(filename=creds_filename)


class FSMState(StatesGroup):
    length = State()
    width = State()
    step_difficult = State()
    color_quantity = State()
    production = State()
    digit_your_name = State()
    digit_your_number = State()
    
    
# da dove parte FSM 
#@dp.message_handler(text="production", state=None)
async def cm_start(query: types.CallbackQuery):
    await FSMState.length.set()
    await query.message.reply('Digit lenght')
    await query.answer()
# catturiamo la prima risposta della lungezza
#@dp.message_handler(state=FSMState.length)
async def load_length(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['length'] = float(message.text)
            await FSMState.next()
        except ValueError:
            await message.reply('Digit a number!')
        await message.reply('Digit width.')
        await message.answer('oooook')
        
# testo per uscire dallo stato FSM
#@dp.message_handler(state="*", commands='Delete')
#@dp.message_hamdler(Text(equals='delete', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
         return
    await state.finish()
    await message.reply('Deleted.')
        
        
        

# catturiamo la seconda risposta della largezza
#@dp.message_handler( state=FSMState.width)
async def load_width(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['width'] = float(message.text)
            await FSMState.next()
        except ValueError:
            await message.reply('Digit a number!')
            return

    await message.reply('Digit color step difficult.')

    list_photos = [
        types.InputMediaPhoto(types.InputFile('img/1.jpg')),
        types.InputMediaPhoto(types.InputFile('img/2.1.jpg')),
        types.InputMediaPhoto(types.InputFile('img/3.jpg')),
    ]
    await message.answer_media_group(list_photos)  
        
        
# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.color_quantity)
async def load_color_quantity(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['step_difficult'] = int(message.text)
            await FSMState.next()
        except ValueError:
            await message.reply('Digit a number!')
        await message.reply('Digit normal or express production.')
        await message.answer('oooook')
        
        

# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.step_difficult)
async def load_step_difficult(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['color_quantity'] = int(message.text)
            await FSMState.next()
        except ValueError :
            await message.answer('digit valid step number')
        await message.reply('Digit color number.')
        await message.answer('oooook')
        
# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.step_difficult)
async def load_production(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        pattern = r'^[a-zA-Z0-9\s]*$'
        match = re.match(pattern, message.text)
        if not match:
            await message.answer('Inserisci una produzione valida.')
            return
        
        data['production'] = str(message.text)
        await FSMState.next()
        await message.reply('Digit your name.')
        await message.answer('oooook')
        
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
        await FSMState.next()
        await message.reply('Digit your phone number +38____---______.')
        await message.answer('oooook')
        
# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.digit_your_number)
async def load_digit_your_number(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        pattern = r'^(\+38)?[0-9]{10}$'
        match = re.match(pattern, message.text)
        if not match:
            await message.answer('Inserisci un numero di telefono valido.')
            return

        try:
            data['digit_your_number'] = int(match.group(0))
        except ValueError:
            await message.answer('Il numero di telefono inserito non è valido.')
            return
        
        # scrivo i dati nel foglio di lavoro
        async def write_to_google_sheets(data):
            gc = init_gspread_client()
            sheet_id = "1ipMDxyuk8U2syXBlg6ZyLoFlLqoeeWEszC2Nw9vWoP0"
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
            [current_date, next_number,data['length'], data['width'], data['color_quantity'], data['step_difficult'], data['production'], data['digit_your_name'], data['digit_your_number']]
            ]
            sheet.insert_rows(values_to_write, 2)
            await message.answer(
                        f"caro {data['digit_your_name']} Lei ha inserito:\n"
                        f"length: {data['length']}\n"
                        f"width: {data['width']}\n"
                        f"step_difficult: {data['step_difficult']}\n"
                        f"color_quantity: {data['color_quantity']}\n"
                        f"produzione: {data['production']}\n"
                    )

        await write_to_google_sheets(data)
        #await message.reply(str(data))   
        await state.finish()
        
        
    
    ###############################################################

# registrazione dei handlers
def register_handlers_state(dp : Dispatcher):
    dp.register_callback_query_handler(cm_start, text="express production", state=None)
    dp.register_message_handler(load_length, state=FSMState.length)
    dp.register_message_handler(cancel_handler, state="*", commands='Delete')
    dp.register_message_handler(cancel_handler, Text(equals='delete', ignore_case=True), state="*")
    dp.register_message_handler(load_width, state=FSMState.width)
    dp.register_message_handler(load_step_difficult, state=FSMState.step_difficult)
    dp.register_message_handler(load_color_quantity, state=FSMState.color_quantity)
    dp.register_message_handler(load_production, state=FSMState.production)
    dp.register_message_handler(load_digit_your_name, state=FSMState.digit_your_name)
    dp.register_message_handler(load_digit_your_number, state=FSMState.digit_your_number)
