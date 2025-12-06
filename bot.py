from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import telegram

# ---------- تنظیمات ربات ----------
BOT_TOKEN = "8285693963:AAGx9Txo6JnYwMb43WqJ6ikWePFGgDlytzQ"
CHANNEL_ID = -1001234567890  # آیدی کانالی که ویدیوها داخل آن است

# ---------- شروع ربات ----------
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🎯 هشتگ‌های پیشنهادی", callback_data="tags")],
        [InlineKeyboardButton("📞 ارتباط با ما", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "سلام دوست عزیز! 😊\n"
        "به ربات «کارشناس فنی گروه MtdArt» خوش اومدی.\n"
        "از منو یکی از گزینه‌ها رو انتخاب کن:",
        reply_markup=reply_markup
    )

# ---------- دکمه‌ها ----------
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "tags":
        tags = (
            "#موشن_گرافیک\n"
            "#بانک_ملت\n"
            "#استوری_موشن\n"
            "#تبلیغاتی\n"
            "#آموزشی\n"
            "#بیلبوردی\n"
            "#پِری_رول"
        )
        query.edit_message_text(
            f"🔍 هشتگ مورد نظرت رو برام بفرست.\n\n"
            f"هشتگ‌های پیشنهادی:\n{tags}"
        )

    if query.data == "contact":
        query.edit_message_text(
            "📞 ارتباط با ما:\n"
            "تلگرام: @yourID\n"
            "اینستاگرام: instagram.com/yourpage\n"
        )

# ---------- دریافت هشتگ ----------
def search_tag(update: Update, context: CallbackContext):
    tag = update.message.text

    update.message.reply_text("⏳ در حال جستجو در کانال...")

    bot = telegram.Bot(token=BOT_TOKEN)

    try:
        posts = bot.get_chat(CHANNEL_ID).messages  # توجه: ممکن است برای تعداد پیام‌ها نیاز به API پیشرفته داشته باشی
    except:
        posts = []

    found = False

    for msg in posts:
        if hasattr(msg, 'caption') and msg.caption and tag in msg.caption:
            found = True
            if hasattr(msg, 'video') and msg.video:
                bot.send_video(chat_id=update.message.chat_id, video=msg.video.file_id, caption=msg.caption)
            elif hasattr(msg, 'photo') and msg.photo:
                bot.send_photo(chat_id=update.message.chat_id, photo=msg.photo[-1].file_id, caption=msg.caption)
            else:
                bot.send_message(chat_id=update.message.chat_id, text=msg.text)

    if not found:
        update.message.reply_text("❌ موردی با این هشتگ پیدا نشد.")

# ---------- اجرای ربات ----------
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_tag))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
