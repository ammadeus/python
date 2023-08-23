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

tools_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
tools_inline_keyboard.row(button1, button2).row(button3, button4) 

#def tools_inline_keyboard():# SECONDA VARIAZIONE DEL keyboard inline del tasto tools
    #inline_keyboard = types.InlineKeyboardMarkup()

    #button1 = types.InlineKeyboardButton(text="Button 1", callback_data="button1")
    #button2 = types.InlineKeyboardButton(text="Button 2", callback_data="button2")

    #inline_keyboard.add(button1, button2)

    #return inline_keyboard
 # keybord del tasto Production diventa inline
#but1 = KeyboardButton('/express виготовлення килимів')
#but2 = KeyboardButton('/стандартне виготовлення килимів')
but1 = InlineKeyboardButton(text="express виготовлення килимів", callback_data="but1")
but2 = InlineKeyboardButton(text="стандартне виготовлення килимів", callback_data="but2")

production_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
production_keyboard.row(but1).row(but2)

# inline keyboard del tasto Learning
butt1 = InlineKeyboardButton(text="онлайн курс", callback_data="butt1")
butt2 = InlineKeyboardButton(text="майстер клас", callback_data="butt2")

learning_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True) 
learning_inline_keyboard.row(butt1).row(butt2)

# inline keyboard del tasto About Us
bt1 = InlineKeyboardButton(text="посилання на соц мереж", callback_data="social")
bt2 = InlineKeyboardButton(text="questions about us", callback_data="questions about us")
bt3 = InlineKeyboardButton(text="відгуки про нас", callback_data="reviews_about_us")

about_us_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
about_us_inline_keyboard.row(bt1).row(bt2).row(bt3)

# inline keyboard question about us(About Us) 
abt1 = InlineKeyboardButton(text="question N.1", callback_data="abt1")
abt2 = InlineKeyboardButton(text="question N.2", callback_data="abt2")
abt3 = InlineKeyboardButton(text="question N.3", callback_data="abt3")

question_about_us_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
question_about_us_inline_keyboard.row(abt1).row(abt2).row(abt3)
#question_about_us_inline_keyboard = types.InlineKeyboardButton("Show New Inline Keyboard", callback_data="question_about_us_inline_keyboard")
# Inline keyboard per la nuova inline keyboard
#question_about_us_inline_keyboard.add(types.InlineKeyboardButton("New Button 1", callback_data="new_button_1"))
#question_about_us_inline_keyboard.add(types.InlineKeyboardButton("New Button 2", callback_data="new_button_2"))

#question_about_us_inline_keyboard = InlineKeyboardMarkup()
#question_about_us_inline_keyboard.add(InlineKeyboardButton("New Button 1", callback_data="new_button_1"))
#question_about_us_inline_keyboard.add(InlineKeyboardButton("New Button 2", callback_data="new_button_2"))

# inline keyboard reviews about us(About Us)
bbt1 = InlineKeyboardButton(text="question N.1", callback_data="bbt1")
bbt2 = InlineKeyboardButton(text="question N.2", callback_data="bbt2")
bbt3 = InlineKeyboardButton(text="question N.3", callback_data="bbt3")

reviews_about_us_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
reviews_about_us_inline_keyboard.row(bbt1).row(bbt2).row(bbt3)

# inline keyboard social(About Us)
cbt1 = InlineKeyboardButton(text="question N.1", callback_data="cbt1")
cbt2 = InlineKeyboardButton(text="question N.2", callback_data="cbt2")
cbt3 = InlineKeyboardButton(text="question N.3", callback_data="cbt3")

social_inline_keyboard  = InlineKeyboardMarkup(resize_keyboard=True)
social_inline_keyboard.row(cbt1).row(cbt2).row(cbt3)