import telebot
bot = telebot.TeleBot("6980680619:AAGma0Bpak9-xzjbmovRZgtVIMa_9AkjTVk")

@bot.message_handler(commands=['start'])

def send_welcome(message):
    bot.send_message(message.chat.id,'Hi')
bot.infinity_polling()    


