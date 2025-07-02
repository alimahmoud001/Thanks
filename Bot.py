import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from flask import Flask

# استخراج المتغيرات من البيئة
TOKEN = os.environ.get('TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# تهيئة تطبيق Flask
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is running!"

async def thank_you(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("شكرا")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, thank_you))
    app.run_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot).start()
    web_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
