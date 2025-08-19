import telebot

# هنا تحط التوكن اللي أخذته من BotFather
TOKEN = "8311648804:AAEdEuCPjp6homSEt6ZXO_rLbiiWT8J-xaE"

bot = telebot.TeleBot(TOKEN)

# دالة تستقبل أي رسالة من المستخدم وترد عليها
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"استلمت رسالتك: {message.text}")

# تشغيل البوت
bot.infinity_polling()
