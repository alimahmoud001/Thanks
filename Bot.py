import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# تهيئة البوت
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحباً! أنا بوت الشكر. أرسل أي رسالة وسأرد بـ "شكرا"')

def thanks_reply(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('شكرا')

def main():
    # الحصول على التوكن من متغير البيئة
    TOKEN = os.getenv("TOKEN", "7906627459:AAFupbP8dosA92dUlWH0DpGvAZK0yGr17b4")
    
    # إنشاء Updater
    updater = Updater(TOKEN)
    
    # تسجيل المعالجين
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, thanks_reply))
    
    # بدء البوت
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == '__main__':
    main()
