from telegram import *
from telegram.ext import *
import Reply

updater = Updater('5464484727:AAFZAolu7UAH5-8J4t3BFp9aA6LDkIpjDhY',use_context= True)

def start(update: Update,context: CallbackContext):
    update.message.reply_text('Hey, there text to interact with me')

def help(update: Update,context: CallbackContext):
    update.message.reply_text("I'm not here to help you")

def messages(update: Update,context: CallbackContext):
    text = str(update.message.text).lower()
    response = Reply.sample_messages(text)
    update.message.reply_text(response)

def error(update: Update,context):
    print(f"Update {update} caused error {context.error}")

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text,messages))
updater.dispatcher.add_error_handler(error)

updater.start_polling()
