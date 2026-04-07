import requests
from ai import text_to_command
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

PC_URL = "http://YOUR_PC_IP:5000/run"
SECRET = "mysecret123"
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # AI → command
    cmd = text_to_command(user_text)

    # Send to PC
    res = requests.post(PC_URL, json={
        "token": SECRET,
        "cmd": cmd
    })

    try:
        output = res.json()
    except:
        output = {"error": "No response"}

    await update.message.reply_text(
        f"🧠 CMD: {cmd}\n\n💻 OUTPUT:\n{output}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()