!pip install python-telegram-bot==12.8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #BotFather, new bot

# находим отца ботов, пишем слэш newbot, и называем своего бота, появляется токен, мы его копируем и вставляем в файл (переменную)

#Способ обращения к боту
TOKEN = '1381537148:AAEhYJtkUuXu-WGzxNXT5AuEm6dOw3DiTAc'

#Создаём бота
updater = Updater(token=TOKEN)

#Диспетчер - штука, которая отвечает за приём и отправку сообщений

dispatcher = updater.dispatcher

#То, что будет происходить при подключении к боту, bot - наш бот, update - что к нам пришло!
def startCommand(bot, update):
  #Тут бот просто отправляет сообщение в чат, у которого id = update.message.chat_id
  bot.send_message(chat_id=update.message.chat_id, text='Привет, я тут!')

def textMessage(bot, update):
    if update.message.text == 'привет':
        bot.send_message(chat_id=update.message.chat_id, text='и тебе привет!')
    if update.message.text == 'пока':
        bot.send_message(chat_id=update.message.chat_id), text='ну, пока!')
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def helpCommand(bot, update):
    bot.send_message(chat_id=update.massage.chat_id)

# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
help_command_handler = CommandHandler('help', helpCommand)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(start_command_handler)

# Начинаем поиск обновлений
updater.start_polling(clean=True)

# Останавливаем бота
updater.idle()