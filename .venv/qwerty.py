import os
from dotenv import load_dotenv
import telebot
import time
import queue
import threading

# Загружаем переменные окружения
load_dotenv()

# Инициализация бота с токеном и ID из переменных окружения
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
user_id = int(os.getenv("TELEGRAM_USER_ID"))

# Инициализация очереди
message_queue = queue.Queue()

# Функция отправки сообщений с задержкой
def send_message_with_delay():
    while True:
        try:
            message = message_queue.get()
            bot.send_message(user_id, message)
            print(f"Отправлено сообщение: {message}")
            time.sleep(1)
        except Exception as e:
            print("Ошибка при отправке сообщения:", e)

# Добавление сообщений в очередь
messages = ["Привет!", "Как дела?", "Это тестовое сообщение", "Очередь работает!"]
for msg in messages:
    message_queue.put(msg)

# Создание и запуск потока для считывателя сообщений
thread = threading.Thread(target=send_message_with_delay)
thread.start()