from aiogram.types import ReplyKeyboardMarkup, KeyboardButton





# bottoni dell'amministratore
button_load = KeyboardButton('/Load')
button_delete = KeyboardButton('/Delete_product')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
            .add(button_delete)