import os
import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# ضع التوكن الخاص بك هنا
TOKEN = "7951407694:AAHUnJHPA34VDtiOw_mYgym04AAJ_Tms-yA"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# تحليل وهمي (تقدر تغيره لاحقاً لتحليل حقيقي للصور)
def analyze_image(photo_path):
    return "شراء سريع ✅"  # تقدر تغير الرد لاحقاً حسب التحليل

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل صورة صفقة، وسيتم تحليلها بإذن الله.")

# عند إرسال صورة
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_path = "last_trade.jpg"
    await file.download_to_drive(file_path)

    result = analyze_image(file_path)
    await update.message.reply_text(result)

# تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    print("البوت يعمل الآن...")
    app.run_polling()
