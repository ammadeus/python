from aiogram.types import ReplyKeyboardMarkup, KeyboardButton# , ReplyKeyboardRemove

b1 = KeyboardButton('/Open')
b2 = KeyboardButton('/Address')
b3 = KeyboardButton('/About Us')
b4 = KeyboardButton('/Learning')
b5 = KeyboardButton('/Production')
b6 = KeyboardButton('/Tools')

kb_client  = ReplyKeyboardMarkup(resize_keyboard=True)#,one_time_keyboard=True)# scompare dopo che premi su

kb_client.row(b1, b2, b3).row(b4, b5, b6)
