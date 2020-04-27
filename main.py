import const
import re
import telebot

cheklist = ('епта', 'сучара', 'хуйня', 'блять')
bot = telebot.TeleBot(const.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    text_message = message.text.lower()
    text_message = re.sub(r'[?|$|.|!|,]', r'', text_message)
    text_message = text_message.split(' ')
    for word in text_message:
        if word in cheklist:
            bot.delete_message(message.chat.id, message.message_id)
            break


if __name__ == '__main__':
    bot.polling(none_stop=True)