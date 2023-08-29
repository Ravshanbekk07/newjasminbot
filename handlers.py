from telegram.ext import callbackcontext
from telegram import (Update,InlineKeyboardMarkup,InlineKeyboardButton)


def start(update:Update,context:callbackcontext):
    btn1=InlineKeyboardButton(text='buyurtmani boshlash',callback_data='buyurtma')
    btn2=InlineKeyboardButton(text='mening savatcham',callback_data='savatcham')
    btn3=InlineKeyboardButton(text='jasmin kontaktlari',callback_data='jasmin kontaktlari')
    btn4=InlineKeyboardButton(text='sozlamalar',callback_data='sozlamalar')
    btn5=InlineKeyboardButton(text='aksiyalar',callback_data='aksiyalar')
    btn6=InlineKeyboardButton(text='buyurtmalarim',callback_data='mybooking')

    inline_keyboard=[[btn1],[btn2],[btn3],[btn4],[btn5],[btn6]]
    first_name=update.message.chat.first_name

    update.message.reply_html(
        text=f"Hello, <b>{first_name}</b>. Xush Kelibsiz \n Sizni Evropa va Milliy restoranining etkazib berish xizmati kutib oladi Jasmin ☘️ \n Sahifani tanlang 👇🏼",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        
    )