
from bussines_brand.models import Advertisments
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = "UserProject.settings"
django.setup()


botName = "Beyond Native Bot"
token = "5406852207:AAEETw_X7Ja0tEj-TFlJDXi8M2thvjDNbhE"

updater = Updater(token, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Hi, {update['message']['chat']['first_name']} I'm  glad to find you here. Tell me how can i help you? use below command to talk with me. Lets Go!
		 	#1 For Latest News/Events/Offer use 'Notify Me' Button
		""")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("Your Message")


def updateme(update: Update, context: CallbackContext):
    i = 0
    data = Advertisments.objects.all()
    msg = f"Well, {update.message.text} Currenntly, {len(data)} offer is available"
    for item in data:
        msg += f"""
		
		{i+1}
			Job Title : {item.name }
			
			Job Description: {item.content if item.content else "No Description avaiable" }
			
			Attached Link : {item.media if item.media else "No Attachments avaiable" }

		"""
        i += 1
    update.message.reply_text(msg)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('updateme', updateme))
updater.dispatcher.add_handler(CommandHandler('help', help))


updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

print("Starting polling...")
updater.start_polling()
