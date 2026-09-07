import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    first_name = message.from_user.first_name if message.from_user else ""
    text = (
        f"ሰላም {first_name} 👋\n\n"
        "እንኳን ወደ Telebirr FraudShield bot በሰላም መጡ! "
        "ከታች Open App የሚለውን በተን በመንካት ማስጀመር ይችላሉ።"
    )
    bot.reply_to(message, text)

@app.route("/", methods=["POST"])
def webhook():
    if request.headers.get("content-type") == "application/json":
        json_string = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Forbidden", 403

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200
