

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

botName = "Beyond Native Bot"
token = '5498779250:AAFch26MWumjBay6WfZDGFULpyPqdlCDOvY'

updater = Updater(token, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hi, welcome to our service !')

def handleReplies (update: Update, context: CallbackContext):
    
    if (update.message.text == '1' ):
        msg='hello'
        update.message.reply_text(msg)
        
    if (update.message.text == '2' ):
        msg='below'
        update.message.reply_text(msg)
        
    if (update.message.text == '3' ):
        msg='kello'
        update.message.reply_text(msg)
        
    if (update.message.text == '4' ):
        msg='jellow'
        update.message.reply_text(msg)
        

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, handleReplies))
print("Starting polling...")
updater.start_polling()

    