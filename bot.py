import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await update.message.reply_text("به ربات خوش آمدید! لطفاً یک هشتگ انتخاب کنید:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"شما {query.data} را انتخاب کردید.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
