from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Ваш токен, полученный от BotFather
TOKEN = '8757031887:AAEW93I_C5U4vpDPXWYzqAQfy3Fz9o4XuUE'


# Функция, которая будет запускаться при вводе команды /start
async def start(update: Update, context: CallbackContext):
    welcome_message = """
🏪 Добро пожаловать!

💰 У нас вы сможете выгодно покупать звёзды и премиум по низкой цене и без KYC.

Актуальные цены:
⭐️ 1 звезда - 1,5₽ | 0,02$

❗️покупка от 50 ⭐️❗️
    """

    # Создание кнопок с актуальными ценами в одной колонке
    keyboard = [
        [InlineKeyboardButton("⭐️ 50 звезд - 75₽ | 0.9$", callback_data='50stars')],
        [InlineKeyboardButton("⭐️ 100 звезд - 149₽ | 1.8$", callback_data='100stars')],
        [InlineKeyboardButton("⭐️ 250 звезд - 374₽ | 4.5$", callback_data='250stars')],
        [InlineKeyboardButton("⭐️ 500 звезд - 747₽ | 9.0$", callback_data='500stars')],
        [InlineKeyboardButton("⭐️ 1000 звезд - 1495₽ | 18.0$", callback_data='1000stars')],
        [InlineKeyboardButton("⭐️ 2500 звезд - 3737₽ | 45.0$", callback_data='2500stars')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопками
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


# Функция для обработки нажатий на кнопки
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()  # Ответ на нажатие кнопки

    # Обработка нажатия на кнопки с количеством звезд
    if query.data == '50stars':
        await query.edit_message_text(text="Вы выбрали 50 звезд за 75₽ | 0.9$. Пожалуйста, подтвердите оплату.")

    elif query.data == '100stars':
        await query.edit_message_text(text="Вы выбрали 100 звезд за 149₽ | 1.8$. Пожалуйста, подтвердите оплату.")

    elif query.data == '250stars':
        await query.edit_message_text(text="Вы выбрали 250 звезд за 374₽ | 4.5$. Пожалуйста, подтвердите оплату.")

    elif query.data == '500stars':
        await query.edit_message_text(text="Вы выбрали 500 звезд за 747₽ | 9.0$. Пожалуйста, подтвердите оплату.")

    elif query.data == '1000stars':
        await query.edit_message_text(text="Вы выбрали 1000 звезд за 1495₽ | 18.0$. Пожалуйста, подтвердите оплату.")

    elif query.data == '2500stars':
        await query.edit_message_text(text="Вы выбрали 2500 звезд за 3737₽ | 45.0$. Пожалуйста, подтвердите оплату.")


# Основная функция для запуска бота
def main():
    # Создаем приложение вместо updater
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд и кнопок
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()