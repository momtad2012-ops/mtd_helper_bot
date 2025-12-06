# bot.py - نسخه اصلاح شده برای Python 3.13 روی Render
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# دریافت توکن از Environment Variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# تابع شروع ربات
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("موشن گرافیک", callback_data='موشن گرافیک')],
        [InlineKeyboardButton("بانک ملت", callback_data='بانک ملت')],
        [InlineKeyboardButton("استوری موشن", callback_data='استوری موشن')],
        [InlineKeyboardButton("تبلیغاتی", callback_data='تبلیغاتی')],
        [InlineKeyboardButton("آموزشی", callback_data='آموزشی')],
        [InlineKeyboardButton("بیلبوردی", callback_data='بیلبوردی')],
        [InlineKeyboardButton("پِری رول", callback_data='پِری رول')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("به ربات خوش آمدید! لطفاً یک هشتگ انتخاب کنید:", reply_markup=reply_markup)

# تابع دکمه‌ها
def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"شما {query.data} را انتخاب کردید.")

# تابع اصلی ربات
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
