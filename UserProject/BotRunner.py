


def ConfigureBot(token, command_plus_replies={"1": "hello", "2": "below", "3": "kello", "4": "jellow"}):
    return f"""

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

botName = "Beyond Native Bot"
token = '{token}'

updater = Updater(token, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hi, welcome to our service !')

def handleReplies (update: Update, context: CallbackContext):
    {genarate_command(command_plus_replies)}

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, handleReplies))
print("Starting polling...")
updater.start_polling()

    """


def genarate_command(command_plus_replies):
    codes = ''
    for cmd, reply in command_plus_replies.items():
        codes += f"""
    if (update.message.text == '{cmd}' ):
        msg='{reply}'
        update.message.reply_text(msg)
        """
    return codes


token = '5498779250:AAFch26MWumjBay6WfZDGFULpyPqdlCDOvY'
codes = ConfigureBot(token)
file = open("newbot.py", "w")
file.write(codes)
file.close()


from newbot import main
main()
