
from aiogram.utils import executor
from create_bot import dp



# funzione per creazione mess. e creazione della Database
async def on_startup(_):
    print("Bot Online!")
    
from handlers import client, admin, other

client.register_handers_client(dp)

    


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)