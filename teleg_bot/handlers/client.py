from aiogram import types, Dispatcher, filters
from create_bot import dp, bot
from keyboards import kb_client, tools_inline_keyboard, production_keyboard, learning_inline_keyboard, about_us_inline_keyboard, question_about_us_inline_keyboard, reviews_about_us_inline_keyboard, social_inline_keyboard, express_production_inline_keyboard
from aiogram.types import  Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData
from data_base import sqlite_db
from aiogram.types.message import ContentType
from data_base.sqlite_db import  DataBase 

db = DataBase('shop_cool.db')
cb = CallbackData('btn', 'type', 'id', 'product_id')



#@dp.message_handler(commands=['contact_us'])
async def contact_us(message: types.Message):
    # Get the administrator ID
    administrators = await bot.get_chat_administrators(message.chat.id)
    # Find the administrator ID
    for administrator in administrators:
        if administrator.is_creator:
            admin_id = administrator.id
            break
        
    await bot.send_message(chat_id=admin_id, text=message.text)
    await message.answer('You can send message to the administrator now.')
    await bot.forward_message(chat_id=admin_id, from_chat_id=message.chat.id)
    
#decoratore che reagisce su /start o /help
#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Hello, I am Kulumkubot. Please press one of the following button.", reply_markup=kb_client)# qua da aggiungere la tastiera)
        await message.delete() # per eliminare mess. non letti
    except:
        await message.reply("Chat with bot in direct: \nhttps://t.me/kulumkubot")
        

#@dp.message_handler(commands=["Tools"])
async def tools_command(message: types.Message):
    #await message.send_message(message.from_user.id, "Please press one of the following button: ", reply_markup=tools_inline_keyboard)
     await bot.send_message(message.from_user.id, "Please press one of the following button: ", reply_markup=tools_inline_keyboard)


#@dp.message_handler(commands=["Production"])
async def production_command(message: types.Message):
     await bot.send_message(message.from_user.id, "Please press one of the following button: ", reply_markup=production_keyboard)
    

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
   
 
#@dp.message_handler(commands=['Shop'])
async def shop_command(message : types.Message):
    #await sqlite_db.sql_read(message)
    read = await sqlite_db.sql_read2()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton(f'Add to cart {ret[1]}', callback_data=f'btn:buy {ret[1]}'))
        kb.add(InlineKeyboardButton(text='Cart', callback_data='cart'))
        await bot.send_message(message.from_user.id,text='press to ', reply_markup=kb)
    try:
        await db.add_users(message.chat.id)
    except Exception as e :
        pass
    
#@dp.callback_query_handler(lambda x: x.data == 'cart')
async def cart(call: types.CallbackQuery):
    await call.answer()
    data = await db.get_cart(call.message.chat.id)
    if not data:
        await call.message.answer("Il tuo carrello è vuoto")
    else:
        new_data = []
        for i in range(len(data)):
            new_data.append(await db.get_user_product(data[i][2]))
        new_data = [new_data[i][0] for i in range(len(new_data))]
        await call.message.answer(f"Il tuo carrello contiene:\n{new_data}")
    

async def gen_products(data, user_id):
    keyboard = InlineKeyboardMarkup()
    for i in data:
        count = await db.get_count_in_cart(user_id, i[1])
        count = 0 if not count else sum(j[0] for j in count)
        keyboard.add(InlineKeyboardButton(text=f'{i[2]}: {i[3]}p - {count}шт',
                                          callback_data=f'btn:plus:{i[1]}:{i[5]}'))
        keyboard.add(InlineKeyboardButton(text='🔽', callback_data=f'btn:minus:{i[1]}:{i[5]}'),
                     InlineKeyboardButton(text='🔼', callback_data=f'btn:plus:{i[1]}:{i[5]}'),
                     InlineKeyboardButton(text='❌', callback_data=f'btn:del:{i[1]}:{i[5]}'))

    return keyboard
        
#@dp.callback_query_handler(lambda x: x.data_ad and x.data_ad. startwith('add '))
async def add_to_cart(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    user_id = call.message.chat.id
    product_id = callback_data.get('id')
    data = await db.add_to_cart(user_id, product_id)
    keyboard = await gen_products(data, call.message.chat.id)
    await call.message.answer(text=f"{product_id} aggiunto al carrello", show_alert=True, reply_markup=keyboard)
    
#@dp.callback_query_handler(cb.filter(type='minus'))
async def minus(call: types.CallbackQuery, callback_data: dict):
    product_id = callback_data.get('product_id')
    count_in_cart = await db.get_count_in_cart(call.message.chat.id, product_id)
    if not count_in_cart or count_in_cart[0][0] == 0:
        await call.message.answer('Cart is empty!')
        return 0
    elif count_in_cart[0][0] == 1:
        await db.remove_one_item(product_id, call.message.chat.id)
    else:
        await db.change_count(count_in_cart[0][0] - 1, product_id, call.message.chat.id)

    data = await db.get_products(callback_data.get('category_id'))
    keyboard = await gen_products(data, call.message.chat.id)

    await call.message.edit_reply_markup(keyboard)

#@dp.callback_query_handler(cb.filter(type='plus'))
async def plus(call: types.CallbackQuery, callback_data: dict):
    product_id = callback_data.get('product_id')
    count_in_cart = await db.get_count_in_cart(call.message.chat.id, product_id)
    await db.change_count(count_in_cart[0][0] + 1, product_id, call.message.chat.id)
    
    data = await db.get_products(callback_data.get('category_id'))
    keyboard = await gen_products(data, call.message.chat.id)

    await call.message.edit_reply_markup(keyboard)
    
#@dp.callback_query_handler(cb.filter(type='del'))
async def delete(call: types.CallbackQuery, callback_data: dict):
    product_id = callback_data.get('product_id')
    count_in_cart = await db.get_count_in_cart(call.message.chat.id, product_id)
    if not count_in_cart:
        await call.message.answer('Cart is empty!')
        return 0
    else:
        await db.remove_one_item(product_id, call.message.chat.id)

    data = await db.get_products(callback_data.get('category_id'))
    keyboard = await gen_products(data, call.message.chat.id)  
    
#dp.message handler(Command('empty'))
async def empty_cart(message: Message):
    await db.empty_cart(message.chat.id)
    await message.answer('Cestino e vuoto!')
    
#dp.message handler(Command('pay'))
async def buy (message: Message):
    data = await db.get_cart(message.chat.id)
    new_data = []
    for i in range(len(data)):
        new_data.append(await db.get_user_product(data[i][2])) 
    new_data = [new_data[i][0] for i in range(len(new_data))]
    await message.answer(new_data)
    await dp.empty_cart(message.chat.id)



"""
#@dp.callback_query_handler(lambda x: x.data_ad and x.data_ad. startwith('add '))
async def add_to_cart(callback_query: types.CallbackQuery):
    product_name = callback_query.data.replace("add ", "")
    user_id = callback_query.message.from_user.id
    await sqlite_db.add_to_cart(product_name, user_id)
    await callback_query.answer(text=f"{product_name} aggiunto al carrello", show_alert=True)

#@dp.callback_query_handler(lambda x: x.data == "cart")
async def cart_button(callback_query: types.CallbackQuery):
    user_id = callback_query.message.from_user.id
    cart = await sqlite_db.get_cart(user_id)
    if not cart:
        callback_query.answer(text="Il carrello è vuoto")
    else:
        products = []
        for product in cart:
            products.append(f"* {product['name']} ({product['quantity']})")

        max_length = 2048

        for i in range(0, len(products), max_length):
            message = "\n".join(products[i:i + max_length])
            await callback_query.answer(text=message)
        #await callback_query.answer(text=message, reply_markup=types.ReplyKeyboardMarkup(row_width=2, keyboard=[
        #    [types.KeyboardButton(text="Svuotare carrello"), types.KeyboardButton(text="Prendere ordine")]
        #]))

#dp.callbaack_query_handler(Command('empty'))
async def empty_cart(message: Message):
    await sqlite_db.empty_cart(message.chat.id)
    await message.answer('il cestino è vuoto')
#deve essere l'ultimo , perche lavora come echo
#@dp.message_handler(state="*")
#async def empty(message : types.Message):
    #await message.answer('Please press any button bellow to speak with bot or press help to contact us')
    #await message.delete() 
"""

def register_handers_client(dp : Dispatcher):
    dp.register_message_handler(contact_us, commands=['contact_us'])
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(tools_command, commands=['Tools'])
    dp.register_message_handler(production_command, commands=["Production"])
    dp.register_message_handler(learning_command, commands=["Learning"])
    dp.register_message_handler(about_us_command, commands=["About"])
    dp.register_message_handler(open_command, commands=["Open"]) 
    dp.register_message_handler(adress_command, commands=["Address"])
    dp.register_callback_query_handler(question_about_us_callback, text='questions about us')
    dp.register_callback_query_handler(reviews_about_us_callback, text='reviews_about_us')
    dp.register_callback_query_handler(social_callback, text='social')
    dp.register_message_handler(shop_command, commands=['Shop'])
    dp.register_callback_query_handler(cart, lambda x: x.data == 'cart')
    dp.register_callback_query_handler(add_to_cart, cb.filter(type='buy'))
    dp.register_callback_query_handler(minus, cb.filter(type='minus'))
    dp.register_callback_query_handler(plus, cb.filter(type='plus'))
    dp.register_callback_query_handler(delete, cb.filter(type='del'))
    #dp.register_callback_query_handler(cart_button, lambda x: x.data == "cart")
    #dp.register_message_handler(empty_cart, commands=['Empty'])
    
    

    