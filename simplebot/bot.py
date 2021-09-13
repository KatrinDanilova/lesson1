#from telegram.ext import Updater
#from telegram.ext import CommandHandler

import logging, os, sys, locale
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

path = 'd:\Python\learn1\simplebot'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename=os.path.join(path, 'bot.log')
)

def start_bot(update: Update, context: CallbackContext):
    myuser = update.message.chat.first_name
    mytext = f"""Привет {myuser}!
 
Я простой бот и понимаю только команду /start
    """
    update.message.reply_text(mytext)
    #print(update) #список полей update
    print(sys.getdefaultencoding())
    print(locale.getpreferredencoding())
    print(sys.stdout)
    print(sys.stderr)

def chat(update: Update, context: CallbackContext):
    mytext = update.message.text
    logging.info(mytext)
    update.message.reply_text(mytext)


def main():
    updtr = Updater('1962228157:AAFEnQahitcgf3WyttR3ZpdUiBLWLQtU0WY', use_context=True)
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    logging.info('Bot started...')
    main()

