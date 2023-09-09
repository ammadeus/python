import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


# Inserisci qui il tuo token ottenuto da BotFather
TOKEN = '6656760098:AAFj8nWawhxGlJlV-tIVSN5TdYByNuH48yI'

# Inizializza il bot e il dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Gestisci il comando /start
@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await message.answer("Ciao! Sono il tuo bot Telegram.")

# Aggiungi altri gestori di comandi o messaggi qui

# Avvia il bot inmodo che ....
if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)








    """
# SOLO ECHO BOT
@dp.message_handler()
async def echo_bot(message : types.Message):
    #await message.answer(message.text)
    #await message.reply(message.text)    #mio mess. piu mess. del bot
    await bot.send_message(message.from_user.id, message.text)   # da errore finche non li scrivi per primo o lo aggiungi
    
# bot che reragisce a una parola 
@dp.message_handler()
async def echo_bot(message : types.Message):
    if message.text == "Ciao":
        await message.answer("rispondo Ciao")
        
        
# decoratore vuoto deve essere sempre in basso, perche cosi puo prendere tutto quello che non hanno preso altri decoratori
@dp.message_handler()
async def echo_bot(message : types.Message):
    if message.text == "Ciao":
        await message.answer("rispondo Ciao")
    #await message.reply(message.text)    #mio mess. piu mess. del bot
    #await bot.send_message(message.from_user.id, message.text)   # da errore finche non li scrivi per primo o lo aggiungi
    
    
    
    
    """