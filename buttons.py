from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# ReplyKeyboardMarkup - Это класс для создания области под кнопки
# KeyboardButton - Это класс для создания кнопки


def menu_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)  # Создали область под кнопки
    btn1 = KeyboardButton(text='Фото дня 🌌')  # Создали Кнопку
    btn2 = KeyboardButton(text='Интересный факт 🪐')  # Создали Кнопку
    btn3 = KeyboardButton(text='Где сейчас МКС?')  # Создали Кнопку
    btn4 = KeyboardButton(text='Астероиды рядом ☄')  # Создали Кнопку
    btn5 = KeyboardButton(text='Restart 🔁')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup
