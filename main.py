import telebot

TOKEN = "8952973971:AAGgrChsLL0sr0jygOWUPeMWFz6vL8rsjgc"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот-модератор.")


@bot.message_handler(commands=['ban'])
def ban(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status

        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} забанен.")
    else:
        bot.reply_to(message, "Используйте команду в ответ на сообщение пользователя.")


@bot.message_handler(func=lambda message: True)
def ban_for_links(message):
    if message.text and "https://" in message.text:
        chat_id = message.chat.id
        user_id = message.from_user.id

        try:
            user_status = bot.get_chat_member(chat_id, user_id).status
            if user_status in ('administrator', 'creator'):
                return
        except Exception:
            return

        try:
            bot.delete_message(chat_id, message.message_id)
        except Exception:
            pass

        bot.ban_chat_member(chat_id, user_id)
        bot.send_message(chat_id, f"Пользователь {message.from_user.first_name} забанен за рекламу.")


bot.polling(non_stop=True)