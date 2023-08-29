
from telegram.ext import Updater,CallbackQueryHandler, CommandHandler, MessageHandler, Filters
import os
from handlers import (
    start,buyurtma,kontaktlar,sozlamalar,aksiyalar,my_booking,savtchammy
)

TOKEN = os.environ['TOKEN']

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(handler=CallbackQueryHandler(buyurtma,pattern='buyurtma'))
    dp.add_handler(handler=CallbackQueryHandler(kontaktlar,pattern='jasmin kontaktlari'))
    dp.add_handler(handler=CallbackQueryHandler(sozlamalar,pattern='sozlamalar'))
    dp.add_handler(handler=CallbackQueryHandler(aksiyalar,pattern='aksiyalar'))
    dp.add_handler(handler=CallbackQueryHandler(my_booking,pattern='mybooking'))
    dp.add_handler(handler=CallbackQueryHandler(savtchammy,pattern='savatcham'))
   
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
