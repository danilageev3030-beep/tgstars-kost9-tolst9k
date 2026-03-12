from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Ваш токен, полученный от BotFather
TOKEN = '8757031887:AAEW93I_C5U4vpDPXWYzqAQfy3Fz9o4XuUE'

# Функция, которая будет запускаться при вводе команды /start
async def start(update: Update, context: CallbackContext):
    welcome_message = """
🏪 Добро пожаловать!

💰 У нас вы сможете выгодно покупать звёзды по низкой цене и без KYC.

Актуальные цены:
⭐️ 1 звезда - 1,5₽ | 0,02$

❗️покупка от 50 ⭐️❗️
    """

    # Кнопки на главной странице с эмодзи
    keyboard = [
        [InlineKeyboardButton("🌟 Купить звезды", callback_data='buy_stars')],
        [InlineKeyboardButton("💬 Поддержка", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопками
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


# Функция для обработки нажатий на кнопки
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()  # Ответ на нажатие кнопки

    try:
        # Кнопка "Купить звезды"
        if query.data == 'buy_stars':
            buy_stars_message = """
Выберите количество звезд для покупки:

⭐️ 50 звезд - 75₽ | 0.9$
⭐️ 100 звезд - 149₽ | 1.8$
⭐️ 250 звезд - 374₽ | 4.5$
⭐️ 500 звезд - 747₽ | 9.0$
⭐️ 1000 звезд - 1495₽ | 18.0$
⭐️ 2500 звезд - 3737₽ | 45.0$
            """

            # Кнопки с ценами на звезды и кнопка "Назад"
            keyboard = [
                [InlineKeyboardButton("⭐️ 50 звезд - 75₽ | 0.9$", callback_data='50stars')],
                [InlineKeyboardButton("⭐️ 100 звезд - 149₽ | 1.8$", callback_data='100stars')],
                [InlineKeyboardButton("⭐️ 250 звезд - 374₽ | 4.5$", callback_data='250stars')],
                [InlineKeyboardButton("⭐️ 500 звезд - 747₽ | 9.0$", callback_data='500stars')],
                [InlineKeyboardButton("⭐️ 1000 звезд - 1495₽ | 18.0$", callback_data='1000stars')],
                [InlineKeyboardButton("⭐️ 2500 звезд - 3737₽ | 45.0$", callback_data='2500stars')],
                [InlineKeyboardButton("🔙 Назад", callback_data='back_to_start')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Отправляем сообщение с кнопками
            await query.edit_message_text(text=buy_stars_message, reply_markup=reply_markup)

        # Кнопка "Поддержка"
        elif query.data == 'support':
            support_message = """
Если у вас возникли проблемы, пожалуйста, обратитесь в нашу службу поддержки.
"""
            keyboard = [
                [InlineKeyboardButton("🔗 Перейти в чат поддержки", url='https://t.me/stars_supp0rt')],
                [InlineKeyboardButton("🔙 Назад", callback_data='back_to_start')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Отправляем сообщение с кнопками
            await query.edit_message_text(text=support_message, reply_markup=reply_markup)

        # Обработка нажатия на кнопки с количеством звезд
        elif query.data in ['50stars', '100stars', '250stars', '500stars', '1000stars', '2500stars']:
            star_price_map = {
                '50stars': '50 звезд за 75₽ | 0.9$',
                '100stars': '100 звезд за 149₽ | 1.8$',
                '250stars': '250 звезд за 374₽ | 4.5$',
                '500stars': '500 звезд за 747₽ | 9.0$',
                '1000stars': '1000 звезд за 1495₽ | 18.0$',
                '2500stars': '2500 звезд за 3737₽ | 45.0$'
            }
            selected_stars = star_price_map[query.data]
            await query.edit_message_text(text=f"Вы выбрали {selected_stars}. Пожалуйста, подтвердите оплату.")

        # Обработка кнопки "Назад"
        elif query.data == 'back_to_start':
            # Используем context.bot.send_message вместо update.message.reply_text
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text="🏪 Добро пожаловать!\n\n💰 У нас вы сможете выгодно покупать звёзды по низкой цене и без KYC.\n\nАктуальные цены:\n⭐️ 1 звезда - 1,5₽ | 0,02$\n\n❗️покупка от 50 ⭐️❗️",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🌟 Купить звезды", callback_data='buy_stars')],
                    [InlineKeyboardButton("💬 Поддержка", callback_data='support')]
                ])
            )

    except Exception as e:
        await query.edit_message_text(text="Произошла ошибка, попробуйте еще раз.")
        print(f"Error: {e}")


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
