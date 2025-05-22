from telebot import TeleBot
from telebot.types import Message
from buttons import menu_buttons
from func_bot import get_apod_photo_info, get_random_space_fact, get_iss_location, get_asteroid

TOKEN = 'YOUR_TOKEN'
NASA_API = 'YOUR_TOKEN'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    username = message.from_user.username
    bot.send_message(chat_id, f'''Здраствуйте{username} Вас приветсвует ASTRO-BOT🚀🌐
Выберете Что вас интересует Нажав на клавиатуру снизу ''', reply_markup=menu_buttons())


MAX_CAPTION_LENGTH = 1024


@bot.message_handler(regexp='Фото дня 🌌')
def get_apod_photo(message):
    chat_id = message.chat.id
    try:
        data = get_apod_photo_info(NASA_API)
        if data.get('media_type') == 'image':
            photo_url = data.get('url')
            title = data.get('title')
            explanation = data.get('explanation')

            caption = f"*{title}*\n\n{explanation}"
            MAX_CAPTION_LENGTH = 1024
            if len(caption) > MAX_CAPTION_LENGTH:
                caption = caption[:MAX_CAPTION_LENGTH - 3] + "..."

            bot.send_photo(chat_id, photo_url, caption=caption, parse_mode='Markdown')
        else:
            bot.send_message(chat_id, "Сегодняшний объект — видео, фото нет.")
    except Exception as e:
        print(f"Ошибка: {e}")


@bot.message_handler(regexp='Интересный факт 🪐')
def send_space_fact(message: Message):
    chat_id = message.chat.id
    try:
        fact = get_random_space_fact(NASA_API)

        # Telegram не позволяет более 4096 символов, но в подписи фото — максимум 1024
        if len(fact) > 4000:
            fact = fact[:3997] + "..."

        bot.send_message(chat_id, fact, parse_mode='Markdown')
    except Exception as e:
        print(f"Ошибка при отправке факта: {e}")
        bot.send_message(chat_id, "Не удалось получить факт. Попробуйте позже.")


@bot.message_handler(regexp='Где сейчас МКС?')
def handle_iss_location(message: Message):
    chat_id = message.chat.id
    msg, lat, lon = get_iss_location()
    if lat is not None and lon is not None:
        try:
            iss_location = get_iss_location()
            bot.send_message(chat_id, get_iss_location())
            bot.send_location(chat_id, lat, lon)
        except:
            bot.send_message(chat_id, text='Не получилось не фартонуло')


@bot.message_handler(regexp='Restart 🔁')
def Restrart(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text='/start')

@bot.message_handler(regexp='Астероиды рядом ☄')
def handle_asrto_location(message: Message):
    chat_id = message.chat.id
    text = get_asteroid()
    bot.send_message(chat_id, text)

bot.polling(none_stop=True)
