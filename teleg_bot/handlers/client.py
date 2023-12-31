from aiogram import types, Dispatcher, filters
from create_bot import dp, bot
from keyboards import kb_client, tools_inline_keyboard, production_keyboard, learning_inline_keyboard, about_us_inline_keyboard, question_about_us_inline_keyboard, reviews_about_us_inline_keyboard, social_inline_keyboard, express_production_inline_keyboard
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher import FSMContext







#decoratore che reagisce su /start o /help
#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Hello, I am Kulumkubot. Please press one of the following button.", reply_markup=kb_client)# qua da aggiungere la tastiera)
        await message.delete() # per eliminare mess. non letti
    except:
        await message.reply("Chat with bot in direct: \nhttps://t.me/kulumkubot")
        
OWNER_ID = '1895279788'
async def send_user_info(user: types.User):
    user_info = f"ID: {user.id}\nName: {user.first_name}\nSurname: {user.last_name}\nUsername: {user.username}"
    await bot.send_message(OWNER_ID, user_info)

#@dp.message_handler(commands=["Tools"])
async def tools_command(message: types.Message):
    #await message.send_message(message.from_user.id, "Please press one of the following button: ", reply_markup=tools_inline_keyboard)
     await bot.send_message(message.from_user.id, "Please press one of the following button: ", reply_markup=tools_inline_keyboard)


#@dp.message_handler(commands=["Production"])
async def production_command(message: types.Message):
     await bot.send_message(message.from_user.id, "Please press one of the following button: ", reply_markup=production_keyboard)
 # Production choice handler
#async def handle_production_choice(message: types.Message):
    #await message.answer("You selected: " + message.text)
    #remove_markup = types.ReplyKeyboardRemove()
    #await message.answer(reply_markup=remove_markup)
    

#@dp.message_handler(commands=["Learning"])
async def learning_command(message: types.Message):
     await bot.send_message(message.from_user.id, "Please press one of the following button: ", reply_markup=learning_inline_keyboard)
     
     
#@dp.message_handler(commands=["About Us"])
async def about_us_command(message: types.Message):
     await bot.send_message(message.from_user.id, "Please press one of the following button: ", reply_markup=about_us_inline_keyboard)



        
# decor. con gg di lavoro
#@dp.message_handler(commands=["Open"])
async def open_command(message : types.Message):
    await bot.send_message(message.from_id, 'Mon - Sat, 9:00 - 20:00')
    
# decor. con indirizzo
#@dp.message_handler(commands=["Address"])
async def adress_command(message : types.Message):
    await bot.send_message(message.from_id, 'Kharkiv...')
    
# keyboard question about us(About Us)
#@dp.message_handler(Text(equal='questions about us'))
#async def question_about_us(message : types.Message):
    #await bot.send_message(message.from_id, "Answer :  ")
#@dp.callback_query_handler(lambda query: query.data == 'questions about us')
#async def question_about_us(callback_query: types.CallbackQuery):
    #await bot.send_message(callback_query.from_user.id, "Here's a new inline keyboard:", reply_markup=question_about_us_inline_keyboard)
#async def show_question_about_us_inline_keyboard(callback_query: types.CallbackQuery):
    #if callback_query.data == "questions about us":
        #await bot.send_message(
            #callback_query.from_user.id,
            #"Here's a new inline keyboard for questions about us:",
            #reply_markup=question_about_us_inline_keyboard,
        #)
 
 # keyboard question about us(About Us)     
#@dp.message(F.text.lower() == 'questions about us')
async def question_about_us_callback(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Here's a new inline keyboard question about us:", reply_markup=question_about_us_inline_keyboard)
 
    
 # keyboard reviews about us(About Us)
 #@dp.message(F.text.lower() == 'reviews_about_us')
async def reviews_about_us_callback(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Here's a new inline keyboard reviews about us:", reply_markup=reviews_about_us_inline_keyboard)
   
   
 # keyboard social(About Us)
 #@dp.message(F.text.lower() == 'social')
async def social_callback(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Here's a new inline keyboard social:", reply_markup=social_inline_keyboard)
   
  
 # keyboard express_production(Production)
 #@dp.message(F.text.lower() == 'social')
#async def express_production_callback(query: types.CallbackQuery):
    #await query.answer()
    #await query.message.answer("Here's a new inline keyboard express production:", reply_markup=express_production_inline_keyboard)
    

    



def register_handers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(tools_command, commands=['Tools'])
    dp.register_message_handler(production_command, commands=["Production"])
    #dp.register_message_handler(handle_production_choice, lambda message: message.text in ["/express виготовлення килимів", "/стандартне виготовлення килимів"])
    dp.register_message_handler(learning_command, commands=["Learning"])
    dp.register_message_handler(about_us_command, commands=["About"])
    dp.register_message_handler(open_command, commands=["Open"]) 
    dp.register_message_handler(adress_command, commands=["Address"])
    dp.register_callback_query_handler(question_about_us_callback, text='questions about us')
    dp.register_callback_query_handler(reviews_about_us_callback, text='reviews_about_us')
    dp.register_callback_query_handler(social_callback, text='social')
    #dp.register_callback_query_handler(express_production_callback, text='express production')
   
    
    #dp.register_callback_query_handler(insert_four_numbers, lambda query: query.data in ["dbt1", "dbt2", "dbt3", "dbt4"])
    #dp.register_callback_query_handler(show_question_about_us_inline_keyboard, lambda query: query.data == 'questions about us')
    #dp.register_message_handler(handle_production_choice)
    