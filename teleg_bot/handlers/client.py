from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


 


#decoratore che reagisce su /start o /help
#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Hello, I am Kulumkubot. Please press one of the following keys.", reply_markup=kb_client)# qua da aggiungere la tastiera)
        await message.delete() # per eliminare mess. non letti
    except:
        await message.reply("Chat with bot in direct: \nhttps://t.me/kulumkubot")
        
# decor. con gg di lavoro
#@dp.message_handler(commands=["Open"])
async def open_command(message : types.Message):
    await bot.send_message(message.from_id, 'Mon - Sat, 9:00 - 20:00')
    
# decor. con indirizzo
#@dp.message_handler(commands=["Address"])
async def adress_command(message : types.Message):
    await bot.send_message(message.from_id, 'Kharkiv...')


def register_handers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=["Open"]) 
    dp.register_message_handler(adress_command, commands=["Address"]) 