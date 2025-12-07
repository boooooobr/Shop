from logic import DB_Managr
from config import *
from telebot import TeleBot
from telebot import types

bot = TeleBot('7689614483:AAG5n7-NSiWPNh3XMYKIwF1aCXqKz_ljPho')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Здравствуйте! Данный бот поможет ответить на ваши вопросы
которые возниклы у вас во вермя заказа на интернет магазины "Все на свете". Команда
/info поможет лучше разобратся как и что делать. 
""")
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
"""
Вот команды которые могут тебе помочь:

/Vopros - отвтить на часто задоваемые вопросы
/Komanda - запишет ваш запрос в базу данных и через кокоето время с вами свяжется спецыолист
""")



@bot.message_handler(commands=['Komanda'])
def soxr(message):
    bot.send_message(message.chat.id, "Напишиет ваш вопрос")
    manager.insert_project
    bot.register_next_step_handler(message, email)
    
def email(message):
    name = message.text
    user_id = message.from_user.id
    data = [user_id, name]
    bot.send_message(message.chat.id, "Напишите вашу почту для того что бы с вами мог связатся специолист")
    
    bot.register_next_step_handler(message,soxpan,data=data)
    
def soxpan(message,data):
    manager.insert_project([tuple(data)])
    bot.send_message(message.chat.id, "Ожидайте ответ в течение 1-2 дней")
        
@bot.message_handler(commands=['Vopros'])
def Rospis(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Как оформить заказ?")
    btn2 = types.KeyboardButton("Как узнать статус моего заказа?")
    btn3 = types.KeyboardButton("Что делать, если товар пришел поврежденным?")
    btn4 = types.KeyboardButton("Как связаться с вашей технической поддержкой?")
    btn5 = types.KeyboardButton("Как отменить заказ?")
    btn6 = types.KeyboardButton("Как узнать информацию о доставке?")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    
    bot.send_message(message.chat.id, """Вот самые часто задаваемые вопросы:
    1. Как оформить заказ?
    2. Как узнать статус моего заказа?
    3. Как отменить заказ?
    4. Что делать, если товар пришел поврежденным?
    5. Как связаться с вашей технической поддержкой?
    6. Как узнать информацию о доставке?""", reply_markup=markup)
    
    bot.register_next_step_handler(message, callback)

@bot.message_handler()
def callback(message):
    if message.text.lower() == 'как оформить заказ?':
        bot.reply_to(message, 'Для оформления заказа, пожалуйста, выберите интересующий вас товар и нажмите кнопку "Добавить в корзину", затем перейдите в корзину и следуйте инструкциям для завершения покупки.')

    elif message.text.lower() == 'как узнать статус моего заказа?':
        bot.reply_to(message, 'Вы можете узнать статус вашего заказа, войдя в свой аккаунт на нашем сайте и перейдя в раздел "Мои заказы". Там будет указан текущий статус вашего заказа.')

    elif message.text.lower() == 'как отменить заказ?':
        bot.reply_to(message, 'Если вы хотите отменить заказ, пожалуйста, свяжитесь с нашей службой поддержки как можно скорее. Мы постараемся помочь вам с отменой заказа до его отправки.')

    elif message.text.lower() == 'что делать, если товар пришел поврежденным?':
        bot.reply_to(message, 'При получении поврежденного товара, пожалуйста, сразу свяжитесь с нашей службой поддержки и предоставьте фотографии повреждений. Мы поможем вам с обменом или возвратом товара.')

    elif message.text.lower() == 'как связаться с вашей технической поддержкой?':
        bot.reply_to(message, 'Вы можете связаться с нашей технической поддержкой через телефон на нашем сайте или написать нам в чат-бота.')

    elif message.text.lower() == 'как узнать информацию о доставке?':
        bot.reply_to(message, 'Информацию о доставке вы можете найти на странице оформления заказа на нашем сайте. Там указаны доступные способы доставки и сроки.')
if __name__ == '__main__':
    manager = DB_Managr(DATABASE)
    bot.infinity_polling()