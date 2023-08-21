from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton# , ReplyKeyboardRemove
from aiogram import types

# keybord principale
b1 = KeyboardButton('/Learning')
b2 = KeyboardButton('/Production')
b3 = KeyboardButton('/Tools')
b4 = KeyboardButton('/Open')
b5 = KeyboardButton('/Address')
b6 = KeyboardButton('/About Us')

kb_client  = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)# scompare dopo che premi su

kb_client.row(b1, b2, b3).row(b4, b5, b6)

# keyboard inline del tasto tools
button1 = InlineKeyboardButton(text="price list на інструменти", callback_data="button1")
button2 = InlineKeyboardButton(text="знижки на інструменти", callback_data="button2")
button3 = InlineKeyboardButton(text="корисні поради(в подарунок налаштування) та гарантії", callback_data="button3")
button4 = InlineKeyboardButton(text="доставка", callback_data="button4")

tools_inline_keyboard = InlineKeyboardMarkup()
tools_inline_keyboard.row(button1, button2).row(button3, button4) 

#def tools_inline_keyboard():# SECONDA VARIAZIONE DEL keyboard inline del tasto tools
    #inline_keyboard = types.InlineKeyboardMarkup()

    #button1 = types.InlineKeyboardButton(text="Button 1", callback_data="button1")
    #button2 = types.InlineKeyboardButton(text="Button 2", callback_data="button2")

    #inline_keyboard.add(button1, button2)

    #return inline_keyboard
 # keybord del tasto Production 
but1 = KeyboardButton('/express виготовлення килимів')
but2 = KeyboardButton('/стандартне виготовлення килимів')

production_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
production_keyboard.row(but1).row(but2)
