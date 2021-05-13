from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import requests
from bs4 import BeautifulSoup
# pip install telegram
# pip install python-telegram-bot

# token
API_TOKEN = '1472625642:AAEK7lAsfTTGHXlnu3BEbJ9mevKZ1PtGWO4'
# updater
updater = Updater(token=API_TOKEN, use_context=True)

def fn_say(text):
    return text
# message handler
def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text

    dividend = fn_say(user_text)
    text = f"내용: {dividend}"
    context.bot.send_message(chat_id=user_id, text=text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
updater.dispatcher.add_handler(echo_handler)

# polling
updater.start_polling()
updater.idle()