from telegram import Bot,Update
from telegram.ext import (CommandHandler,
    Dispatcher,CallbackQueryHandler)
import os 
from handlers import (start,buyurtma,kontaktlar,sozlamalar,my_booking,
                      aksiyalar,savtchammy)

from flask import Flask,request

app=Flask(__name__)
TOKEN=os.environ.get('TOKEN')
bot =Bot(TOKEN)

@app.route('/webhook/',methods=['POST'])
def main():
    dis=Dispatcher(bot,None,workers=0)
    data=request.get_json(force=True)
    update=Update.de_json(data=data,bot=bot)
    dis.add_handler(handler=CommandHandler('start',start))
    
    dis.add_handler(handler=CallbackQueryHandler(
        buyurtma, pattern="buyurtma"))
    dis.add_handler(handler=CallbackQueryHandler(
        kontaktlar, pattern="jasmin kontaktlari"))
    dis.add_handler(handler=CallbackQueryHandler(
        sozlamalar, pattern="sozlamalar"))
    dis.add_handler(handler=CallbackQueryHandler(
        my_booking, pattern="mybooking"))
    dis.add_handler(handler=CallbackQueryHandler(
        aksiyalar, pattern="aksiyalar"))
    dis.add_handler(handler=CallbackQueryHandler(
        savtchammy, pattern="savatcham"))

    dis.process_update(update)
    return 'cool'


@app.route('/')
def home():
    return 'runing well'


@app.route('/set-webhook/')
def set_hook():

    r = bot.set_webhook('https://jasmintaom.pythonanywhere.com/webhook/')
    return f'info:{r}'


   