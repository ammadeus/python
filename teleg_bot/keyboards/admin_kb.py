from aiogram.types import ReplyKeyboardMarkup, KeyboardButton





# bottoni dell'amministratore
button_load = KeyboardButton('/Load')
button_delete = KeyboardButton('/Delete_product')
button_back = KeyboardButton('/Back')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)
button_case_admin.add(button_load, button_back)
button_case_admin.add(button_delete)