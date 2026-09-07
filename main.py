import os
import telebot

# የቦት Token ከ Render Environment Variable ይቀበላል
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


# ተጠቃሚው /start ሲል የሚሰራ ተግባር
@bot.message_handler(commands=["start"])
def send_welcome(message):
    # የተጠቃሚውን የቴሌግራም ስም ይወስዳል
    first_name = message.from_user.first_name

    # ቦቱ የሚመልሰው መልእክት
    text = (
        f"ሰላም {first_name} 👋\n\n"
        "እንኳን ወደ Telebirr FraudShield bot በሰላም መጡ! "
        "ከታች Open App የሚለውን በተን በመንካት ማስጀመር ይችላሉ።"
    )

    bot.reply_to(message, text)


# ቦቱ ሁልጊዜ ክፍት ሆኖ መልእክት እንዲቀበል
if __name__ == "__main__":
    bot.infinity_polling()
