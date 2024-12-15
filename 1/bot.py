import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Определяем команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш новый бот.')

# Основная функция
def main():
    # Вставьте сюда ваш токен
    TOKEN =7890275951:AAFn5bTeKOy-VwjDB7btNHdnrP-5ir8WXhw 
    
    # Создаем Updater и передаем ему токен
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчика команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()

if __name__ == '__main__':
    main()