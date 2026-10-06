import telebot

bot = telebot.TeleBot('8952973971:AAGgrChsLL0sr0jygOWUPeMWFz6vL8rsjgc')

@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, "Я эхобот, повторяю все, что ты напишешь")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, m.text)
    

bot.polling()