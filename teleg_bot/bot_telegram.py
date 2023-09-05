
from aiogram.utils import executor
from create_bot import dp



# funzione per creazione mess. e creazione della Database
async def on_startup(_):
    print("Bot Online!")
    
from handlers import client, state,state_express, other

client.register_handers_client(dp)
state.register_handlers_state(dp)
state_express.register_handlers_state_express(dp)

    


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)