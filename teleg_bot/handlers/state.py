from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text 



class FSMState(StatesGroup):
    length = State()
    width = State()
    color_quantity = State()
    step_difficult = State()
    
    
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
        data['length'] = float(message.text)
        await FSMState.next()
        await message.reply('Digit width.')
        
        
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
async def load_width(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['width'] = float(message.text)
        await FSMState.next()
        await message.reply('Digit color quantity.')
        
        
# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.color_quantity)
async def load_color_quantity(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['color_quantity'] = float(message.text)
        await FSMState.next()
        await message.reply('Digit color step difficult.')
        
        

# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.step_difficult)
async def load_step_difficult(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['step_difficult'] = float(message.text)
    
    async with state.proxy() as data:
        await message.reply(str(data))   
    await state.finish()
    
    
    ###############################################################
    
    

               

# registrazione dei handlers
def register_handlers_state(dp : Dispatcher):
    dp.register_callback_query_handler(cm_start, text="production", state=None)
    dp.register_message_handler(load_length, state=FSMState.length)
    dp.register_message_handler(cancel_handler, state="*", commands='Delete')
    dp.register_message_handler(cancel_handler, Text(equals='delete', ignore_case=True), state="*")
    dp.register_message_handler(load_width, state=FSMState.width)
    dp.register_message_handler(load_color_quantity, state=FSMState.color_quantity)
    dp.register_message_handler(load_step_difficult, state=FSMState.step_difficult)
    
    
    