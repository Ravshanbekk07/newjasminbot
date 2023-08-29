from telegram import Bot,Update
from telegram.ext import (Commandhandler,
    Dispatcher,CallbackQueryHandler)
import os 
from handlers import (start)

from flask import Flask,request
TOKEN=os.environ.get('TOKEN')
bot =Bot(TOKEN)

app=Flask(__name__)

@app.route('/webhook/',methods=['POST'])
def main():
    dis=Dispatcher(bot,None,workers=0)
    data=request.get_json(force=True)
    update=Update.de_json(data=data,bot=bot)
    dis.add_handler(handler=Commandhandler('start',start))


    dis.process_update(update)
    return 'cool'