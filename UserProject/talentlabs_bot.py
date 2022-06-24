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


def ButtonGenarator(obj, btn_type):
    btns_list = obj
    widget_list = []
    j = 0
    for i in btns_list:
        widget_list.append(
            [InlineKeyboardButton(i, callback_data=str(btn_type))])
    return widget_list


data = fetch_data()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("Yes, I'm Excited", callback_data=str(ONE)),
            InlineKeyboardButton(
                "A bit confused but let's get started", callback_data=str(ONE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text(f"Hi, <b> {update['message']['chat']['first_name']} !</b> Welcome to <u>Talent native bot ! </u> lets get started? But, first i required some information about yourself. <b> Ready? </b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    industry = data['job_industry_option'].split(',')[1:]
    keyboard = ButtonGenarator(industry, TWO)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="What Job Industry Or Carrer you are looking for ? Please Choose one", reply_markup=reply_markup
    )
    return START_ROUTES


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    print(query.data)
    job_skill = data['job_skills_options'].split(',')[1:]
    keyboard = ButtonGenarator(job_skill, THREE)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Which skill describe you best ? Please Choose one", reply_markup=reply_markup
    )
    return START_ROUTES


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    print(query.data)
    keyboard = [
        [
            InlineKeyboardButton(i, callback_data=str(FOUR)) for i in data['experince_options'].split(',')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="So its final question . How many years of experince you have?", reply_markup=reply_markup)
    return START_ROUTES


async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    print(query.data)
    keyboard = [[InlineKeyboardButton("FINISH", callback_data=str(FIVE))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="So Lets Finsih it !", reply_markup=reply_markup
    )
    return END_ROUTES


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
ConversationHandler that the conversation is over.
"""
    query = update.callback_query
    await query.answer()
    print(query.data)
    await query.edit_message_text(text=f"Well Done! you reached the end. Hope this has been a great experience for you press /findjob to see suitable job", parse_mode=ParseMode.HTML)
    return ConversationHandler.END


async def getMatchedJob(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    industry = ""
    # ?job_industry={industry}&job_skill={skill}
    skill = ""
    api = "http://localhost:8000/api/get/job-application-data/"
    r = requests.get(api)
    data = r.json()[:3]
    msg = ""
    i = 0
    for job in data:
        msg += f"""#JOB {i+1} 
Job Title: { 'N/A' if job['job_title'] == "Please choose an option" else job['job_title'] }
Job Description: {job['job_description']}
Job Vacancy: {job['job_vacancy']}
Job location: {job['job_location']}
Working days: {job['working_days']}
Working hours: {job['working_hours']}
job type: {'N/A' if job['job_type'] == "Please choose an option" else job['job_title'] }
job industry: {'N/A' if job['job_industry'] == "Please choose an option" else job['job_industry']}
salary expectation: {job['salary_expectation']}
Pay Rate Type: {'N/A' if  job['job_pay_rate_type']== "Please choose an option" else job['job_pay_rate_type']}
Experince Require: {job['required_job_experince']}
Require job skill: {'N/A' if  job['require_job_skill']== "Please choose an option" else  job['require_job_skill'] }
		\n
		"""
        i += 1
        if msg == "":
            msg = "Based On Your Data No Job/offers found Found"
    await update.message.reply_text(msg)


def main() -> None:
    application = Application.builder().token(tlb).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(three, pattern="^" + str(THREE)+"$"),
                CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"),
            ],
            END_ROUTES: [
                CallbackQueryHandler(end, pattern="^" + str(FIVE) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("findjob", getMatchedJob))
    application.run_polling()


if __name__ == "__main__":
    main()

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
