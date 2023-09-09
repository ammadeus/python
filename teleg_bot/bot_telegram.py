
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db




# funzione per creazione mess. e creazione della Database
async def on_startup(_):
    print("Bot Online!")
    sqlite_db.sql_start()
    
from handlers import client, state,state_express,state_circle, admin,  other

client.register_handers_client(dp)
state.register_handlers_state(dp)
state_express.register_handlers_state_express(dp)
state_circle.register_handlers_state_circle(dp)
admin.register_handlers_state_ad(dp)

    


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)