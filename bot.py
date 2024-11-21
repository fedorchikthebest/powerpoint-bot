from TOKEN import TOKEN
from parser.parser import generate_presentation
import os
import telebot
import time
import threading, queue

bot = telebot.TeleBot(TOKEN)
q = []
used = []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, пришли мне промт для презентации, а я скину презентацию")


@bot.message_handler(commands=['stop'])
def stop_message(message):
    if message.chat.id in used:
        i = used.index(message.chat.id)
        used.pop(i)
        q.pop(i)
        bot.send_message(message.chat.id, "Мы удалили ваш запрос")
    else:
        bot.send_message(message.chat.id, "Ваш запрос не найден, либо уже в обработке.")



@bot.message_handler(content_types='text')
def message_reply(message):
    if message.chat.id in used:
        bot.send_message(message.chat.id, "Вы уже сделали запрос, ждите")
    else:
        bot.send_message(message.chat.id, f"Вы на {len(q) + 1} месте в очереди. Подождите генерации")
        q.append([message.text, message.chat.id])
        used.append(message.chat.id)


def worker():
    while True:
        if len(q) == 0:
            time.sleep(5)
            continue
        item = q[0]
        q.pop(0)
        used.pop(0)
        try:
            generate_presentation(item[0])
            link = f"{os.getcwd()}/presentations/{os.listdir('presentations/')[1]}"
            a = open(link, "rb")
            bot.send_document(item[1], a)
            a.close()
            os.remove(link)
        except Exception:
            bot.send_message(item[1], "Произошла ошибка при создании презентациию Попробуйте снова")


threading.Thread(target=worker, daemon=True).start()

bot.infinity_polling()
