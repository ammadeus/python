from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


# EXPRESS PRODUCTION

class FSMState(StatesGroup):
    length_express = State()
    width_express = State()
    color_quantity_express = State()
    step_difficult_express = State()
    
    
# da dove parte FSM 
#@dp.message_handler(text="production", state=None)
async def cm_start_express(query: types.CallbackQuery):
    await FSMState.length_express.set()
    await query.message.reply('Digit lenght')
    await query.answer()
# catturiamo la prima risposta della lungezza
#@dp.message_handler(state=FSMState.length)
async def load_length_express(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['length_express'] = float(message.text)
        await FSMState.next()
        await message.reply('Digit width.')
        

# catturiamo la seconda risposta della largezza
#@dp.message_handler( state=FSMState.width)
async def load_width_express(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['width_express'] = float(message.text)
        await FSMState.next()
        await message.reply('Digit color quantity.')
        
        
# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.color_quantity)
async def load_color_quantity_express(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['color_quantity_express'] = float(message.text)
        await FSMState.next()
        await message.reply('Digit color step difficult.')
        
        

# catturiamo la terza risposta della color_quantity
#@dp.message_handler(state=FSMState.step_difficult)
async def load_step_difficult_express(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['step_difficult_express'] = float(message.text)
    
    async with state.proxy() as data_express:
        await message.reply(str(data_express))   
    await state.finish()
    
    
# registrazione dei handlers
def register_handlers_state_express(dp : Dispatcher):
    dp.register_callback_query_handler(cm_start_express, text="express production", state=None)
    dp.register_message_handler(load_length_express, state=FSMState.length_express)
    dp.register_message_handler(load_width_express, state=FSMState.width_express)
    dp.register_message_handler(load_color_quantity_express, state=FSMState.color_quantity_express)
    dp.register_message_handler(load_step_difficult_express, state=FSMState.step_difficult_express)