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
button1 = InlineKeyboardButton(text="Pulsante 1", callback_data="button1")
button2 = InlineKeyboardButton(text="Pulsante 2", callback_data="button2")

tools_inline_keyboard = InlineKeyboardMarkup()
tools_inline_keyboard.add(button1, button2)  

#def tools_inline_keyboard():
    #inline_keyboard = types.InlineKeyboardMarkup()

    #button1 = types.InlineKeyboardButton(text="Button 1", callback_data="button1")
    #button2 = types.InlineKeyboardButton(text="Button 2", callback_data="button2")

    #inline_keyboard.add(button1, button2)

    #return inline_keyboard