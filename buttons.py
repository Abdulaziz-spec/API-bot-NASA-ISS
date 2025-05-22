from telebot.types import ReplyKeyboardMarkup, KeyboardButton



def menu_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)  
    btn1 = KeyboardButton(text='Фото дня 🌌') 
    btn2 = KeyboardButton(text='Интересный факт 🪐')  
    btn3 = KeyboardButton(text='Где сейчас МКС?') 
    btn4 = KeyboardButton(text='Астероиды рядом ☄') 
    btn5 = KeyboardButton(text='Restart 🔁')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup
