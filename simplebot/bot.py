# -*- coding: utf-8 -*-
#from telegram.ext import Updater
#from telegram.ext import CommandHandler

import logging, os, sys, locale
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import settings
import ephem, datetime

path = 'd:\Python\learn1\simplebot'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename=os.path.join(path, 'bot.log')
)

def start_bot(update: Update, context: CallbackContext):
    myuser = update.message.chat.first_name
    mytext = f"""Привет {myuser}! Я простой бот и понимаю только команду /start"""
    logging.info(f"Пользователь {update.message.chat.username} нажал /start")
    update.message.reply_text(mytext)
    #print(update) #список полей update
    #print(sys.getdefaultencoding())
    #print(locale.getpreferredencoding())
    #print(sys.stdout)
    #print(sys.stderr)

def chat(update: Update, context: CallbackContext):
    
    planet_list = {'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Sun', 'Moon'}
    mytext = update.message.text
    logging.info(b'%s'.decode('utf-8') % (mytext)) # в этом месте идет неправильное логирование

    if mytext in planet_list:
        if mytext == 'Mercury':
            planet = ephem.Mercury(datetime.date.today())
        elif mytext == 'Venus':
            planet = ephem.Venus(datetime.date.today()) 
        elif mytext == 'Mars':
            planet = ephem.Mars(datetime.date.today()) 
        elif mytext == 'Jupiter':
            planet = ephem.Jupiter(datetime.date.today())
        elif mytext == 'Saturn':
            planet = ephem.Saturn(datetime.date.today())
        elif mytext == 'Uranus':
            planet = ephem.Uranus(datetime.date.today())
        elif mytext == 'Neptune':
            planet = ephem.Neptune(datetime.date.today())
        elif mytext == 'Pluto':
            planet = ephem.Pluto(datetime.date.today())
        elif mytext == 'Sun':
            planet = ephem.Sun(datetime.date.today())    
        elif mytext == 'Moon':
            planet = ephem.Moon(datetime.date.today())    

        constellation = ephem.constellation(planet)
        update.message.reply_text(f"Сегодня планета {mytext} в созвездии {constellation}")
    else: 
        update.message.reply_text(mytext)



def main():
    updtr = Updater(settings.TELEGRAM_API_KEY, use_context=True)
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    logging.info('Bot started...')
    main()

