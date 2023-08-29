from telegram.ext import CallbackContext
from telegram import (Update,InlineKeyboardMarkup,InlineKeyboardButton)


def start(update:Update,context:CallbackContext):
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


def buyurtma(update:Update,context:CallbackContext):
    
    btn1 = InlineKeyboardButton(
        text='sovuq gazaklar', callback_data='sovuq gazaklar ')
    btn2 = InlineKeyboardButton(
        text='issiq gazaklar', callback_data='issiq gazak')
    btn3 = InlineKeyboardButton(text='biznes lanch', callback_data='lanch')
    btn4 = InlineKeyboardButton(text='salatlar', callback_data='salatlar')
    btn5 = InlineKeyboardButton(text='sho\'rva', callback_data='sho\'rva')
    btn6 = InlineKeyboardButton(
        text='uygur taomlari', callback_data='uygur taomlari')
    btn7 = InlineKeyboardButton(text='milliy taomlar', callback_data='milliy')
    btn8 = InlineKeyboardButton(
        text='evropa taomlari', callback_data='evropa taomlari')
    btn9 = InlineKeyboardButton(text='pizza', callback_data='pizza')
    btn10 = InlineKeyboardButton(
        text='maxsus shefdan', callback_data='maxsus shefdan')
    btn11 = InlineKeyboardButton(text='six kabob', callback_data='six kabob')
    btn12 = InlineKeyboardButton(text='bezaklar', callback_data='bezaklar')
    btn13 = InlineKeyboardButton(text='non', callback_data='non')
    btn14 = InlineKeyboardButton(text='ichimlik', callback_data='ichimlik')
    btn15 = InlineKeyboardButton(text='samsa', callback_data='samsa')
    btn16 = InlineKeyboardButton(text='pivo', callback_data='pivo')
    btn17 = InlineKeyboardButton(text='fast food', callback_data='fast food')


    inline_keyboard=[btn1,btn2,btn3,btn4,btn5,btn6,
                     btn7,btn8,btn9,btn10,btn11,btn12,
                     btn13,btn14,btn15,btn16,btn17]
    keyboards=[]
    rows=[]
    for btn in inline_keyboard:
        rows.append(btn)
        if len(rows)==3:
            keyboards.append(rows)
            rows=[]
    if rows:
        keyboards.append(rows)
    
    update.callback_query.message.reply_html(
        text=f"<b>Sahifani tanlang👇🏼</b>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboards)
    )


def kontaktlar(update:Update,context:CallbackContext):
    btn1 = InlineKeyboardButton(text='instagram', url='https://instagram.com')
    btn2 = InlineKeyboardButton(text='kanal', url='https://t.me/Stranger070')
    btn3 = InlineKeyboardButton(
        text='boglanish', url='https://t.me/Stranger070')
    btn4 = InlineKeyboardButton(
        text='tavsiyalash', url='https://t.me/Stranger070')
    inline_keyboard=[[btn1, btn2], [btn3, btn4]]

    update.callback_query.message.reply_html(
        text=f"<b>Jasmin restaraunt</b>.\n+998934526621\n +998936252712 \n 🏠 Manzil:  Ул. Амира Темура 202, ориентир «SAMAUTO»\n⏳Ish vaqti:  10:00 - 22:00 (Yopiq) \n👨🏻‍🍳🍢🍲👨🏻‍🍳🍢🍲👨🏻‍🍳🍢🍲👨🏻‍🍳🍢🍲👨🏻‍🍳",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )

def sozlamalar(update:Update,context:CallbackContext):
    btn1=InlineKeyboardButton(text="o'zbek",callback_data="o'zbek")
    btn2 = InlineKeyboardButton(text='русский', callback_data='русский')
    inline_keyboard=[[btn1],[btn2]]

    update.callback_query.message.reply_html(
        text=f'tilni tanlang',
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )