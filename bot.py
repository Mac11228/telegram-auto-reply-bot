from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8686144572:AAHDKe2p540asJEdV2UH21MT3TmjcXhGU4g"

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
👋 Welcome!

What can this channel do?

✅ Manufacturer & Wholesaler
✅ High Purity Products
✅ Reliable Supply
✅ Discreet Shipping Worldwide
✅ Lab Use Only

📩 Contact for videos and pictures:

Telegram: @chinasupply98

Signal:
https://signal.me/#eu/6EqFuDg0mv6LTc4OnNvJ0wGR2zPZwhenbMCJ88ZP5ziQ0cyM1XZBqanXLTwex24k
""")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Bot is running...")
app.run_polling()
