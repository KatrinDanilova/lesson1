#from telegram.ext import Updater
#from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

def start_bot(update: Update, context: CallbackContext):
    myuser = update.message.chat.first_name
    mytext = f"""Привет {myuser}!
 
Я простой бот и понимаю только команду /start
    """
    update.message.reply_text(mytext)
    print(update)


def main():
    updtr = Updater('1962228157:AAFEnQahitcgf3WyttR3ZpdUiBLWLQtU0WY', use_context=True)
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    main()

