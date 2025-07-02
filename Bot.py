import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# توكن البوت الخاص بك
TOKEN = "7906627459:AAFupbP8dosA92dUlWH0DpGvAZK0yGr17b4"
# معرف المحادثة (chat_id)
CHAT_ID = 910021564

# إعداد تسجيل الأخطاء
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """يرسل رسالة ترحيبية عند استخدام الأمر /start."""
    user = update.effective_user
    await update.message.reply_text(f"مرحبًا {user.first_name}! أنا بوت بسيط. فقط سأشكرك عندما ترسل أي رسالة.")

async def thank_you(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """يرد على الرسائل بكلمة شكرًا."""
    await update.message.reply_text("شكرا")

def main() -> None:
    """تشغيل البوت."""
    # إنشاء التطبيق وتمرير توكن البوت.
    application = Application.builder().token(TOKEN).build()

    # معالج للأمر /start
    application.add_handler(CommandHandler("start", start))

    # معالج للرسائل النصية العادية (كل نص ليس أمرًا)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, thank_you))

    # تشغيل البوت حتى يتم الضغط على Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
