from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
    print(update.message.text)
    
def sayName(update: Update, context: CallbackContext):
    name = update.message.text
    
    split_name = name.split(' ')
    name = split_name[1]
    
    # print(name.split(" "))
    # print(name.lower())
    
    # 334123-1238428-1239438
    
    update.message.reply_text(f'Hello, {name}')
    
    

updater = Updater('5386329288:AAE34vd8YLgHpJ-VUNKSKKQFGHhjurzjf6U')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('sayname', sayName))

updater.start_polling()
updater.idle()