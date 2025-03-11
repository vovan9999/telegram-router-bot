import requests
import telebot

TOKEN = "7225625963:AAHN6T7KLshjsX5R-v_6ZY_Q7Zvpx2NmoDQ"
ROUTER_IP = "myrouterxiaomi.ddns.net"  # Наприклад, 93.184.216.34

# Створюємо екземпляр бота
bot = telebot.TeleBot(TOKEN)

# Функція для створення інлайн клавіатури з кнопкою
def create_inline_keyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton("Перевірити роутер", callback_data="check_router")
    markup.add(button)
    return markup

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    # Відправляємо повідомлення з кнопкою
    bot.send_message(message.chat.id, "Привіт! Натисни кнопку, щоб перевірити, чи роутер в мережі.", reply_markup=create_inline_keyboard())

# Обробка натискання на кнопку
@bot.callback_query_handler(func=lambda call: call.data == "check_router")
def check_router(call):
    # Логіка перевірки статусу роутера
    router_status = "Роутер в мережі ✅"  # Можна змінити логіку на реальну перевірку
    
    # Відповідаємо на натискання кнопки
    bot.answer_callback_query(call.id, text=router_status)
    bot.send_message(call.message.chat.id, router_status, reply_markup=create_inline_keyboard())

# Запускаємо бота
bot.polling(none_stop=True)