import os
import telebot
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Setup Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_pc_api(action: str, params: str = ""):
    """This tool allows Gemini to control the PC."""
    url = f"{os.getenv('PC_SERVER_URL')}/execute"
    headers = {"x-token": os.getenv("AUTH_TOKEN")}
    payload = {"action": action, "params": params}
    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash', 
    tools=[call_pc_api]
)
chat = model.start_chat(enable_automatic_function_calling=True)

# Setup Telegram
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(func=lambda m: True)
def handle_msg(message):
    try:
        response = chat.send_message(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

print("AI Bridge is running...")
bot.infinity_polling()