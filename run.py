
from telegram.ext import Updater,CallbackQueryHandler, CommandHandler, MessageHandler, Filters
import os
from handlers import (
    start,buyurtma
)

TOKEN = os.environ['TOKEN']

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(handler=CallbackQueryHandler(buyurtma,pattern='buyurtma'))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
