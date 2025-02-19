from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

# Ваш реальный токен бота
TELEGRAM_TOKEN = '7812964670:AAHeoDOxJof_CSvT-SGJg2PyOMXoopeX07s'

# Функция для обработки команды /start
async def start(update, context):
    # Ссылка на React-приложение через HTTPS (ngrok)
    keyboard = [
        [InlineKeyboardButton(
            "Открыть приложение", 
            web_app={'url': 'https://3359-57-129-28-95.ngrok-free.app'}  
        )]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text('Привет! Нажми кнопку, чтобы открыть приложение.', reply_markup=reply_markup)

# Главная функция для запуска бота
def main():
    # Инициализируем бота с реальным токеном
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Регистрируем обработчик для команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
