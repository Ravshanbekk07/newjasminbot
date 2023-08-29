
from telegram.ext import Updater,CallbackQueryHandler, CommandHandler, MessageHandler, Filters
import os
from handlers import (
    start,buyurtma,kontaktlar,sozlamalar
)

TOKEN = os.environ['TOKEN']

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(handler=CallbackQueryHandler(buyurtma,pattern='buyurtma'))
    dp.add_handler(handler=CallbackQueryHandler(kontaktlar,pattern='jasmin kontaktlari'))
    dp.add_handler(handler=CallbackQueryHandler(sozlamalar,pattern='sozlamalar'))
   
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
