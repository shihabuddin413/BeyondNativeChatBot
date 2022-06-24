import requests
from channels.db import database_sync_to_async
from concurrent.futures import thread
from tokens import tlb
import logging
from telegram import __version__ as TG_VER
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    CallbackContext,
    ConversationHandler,
)

from tokens import bnb

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
ONE, TWO, THREE, FOUR, FIVE = range(5)

UserProfile = {
    "interect_permission": True,
    "job_industry": "",
    "job_skill": "",
    "experince": ""
}


def fetch_data():
    r = requests.get('http://localhost:8000/api/get/all-options-data/')
    data = r.json()
    return data[0]


data = fetch_data()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("Notify ME", callback_data=str(ONE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text(f"""Hi, {update['message']['chat']['first_name']} I'm  glad to find you here. Lets Go For it! Find Latest News/Events/Offer through <b>Notify Me</b> Button """, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    return START_ROUTES


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    api = "http://localhost:8000/api/get/content/"
    r = requests.get(api)
    data = r.json()[:5]
    data = data[:5] if len(data) > 5 else data
    msg = f"We found {len(data)} new offers but restricted to 5 due to telegram rules \n "
    keyboard = [
        [
            InlineKeyboardButton("Next", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    i = 0
    for item in data:
        msg += f"""

		{i+1}
			Job Title : { item['name'] }

			Job Description: { item['content'] if item['content'] else "No Description avaiable" }

			Attached Link : { item['media'] if item['media'] else "No Attachments avaiable" }

		"""
        i += 1
        if msg == "":
            msg = "Based On Your Data No Job/offers found Found ... "
    await query.edit_message_text(msg, reply_markup=reply_markup)
    return END_ROUTES


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    url = "https://t.me/TalentNativeBot"
    await query.answer()
    reply_markup = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text="Continue here!", url=url)
    )
    await query.edit_message_text(
        text="Hey this is the time to look for a job and its become when you make it happen with out Talent Native. A perfect bot to find a awesome job for you ! to connect press below button\n Mainwhile, you can always use START button above top corner or /start command to find the latest update through Notify button", reply_markup=reply_markup
    )
    return ConversationHandler.END


def main() -> None:
    application = Application.builder().token(bnb).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
            ],
            END_ROUTES: [
                CallbackQueryHandler(end, pattern="^" + str(TWO) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
