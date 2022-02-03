from raises import ConvExeption, WrongTransaction
from support import keys,keys_top, TOKEN, HELP
import telebot
from decimal import Decimal

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, f"Приветствую {message.from_user.full_name}! \nПомощь - /help, \nСписок TOP100 валют - /values")


@bot.message_handler(commands=['help'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, HELP)

@bot.message_handler(commands=['report'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, 'Благодарим за обращение,по обработке обращение,мы с вами свяжемся.')


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    for cur in keys_top.items():
        text = "\n".join((text, (f'{cur[0]} - {cur[1]}')))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    name = message.from_user.full_name
    try:
        inputed_values = message.text.upper().split(' ')
        if len(inputed_values) != 3:
            raise ConvExeption('Incorrect input data: Введите запрос в формате с одним пробелом без запятых: валюта1 валюта2 колл-во едениц ')
        curr_from, curr_to, amount = inputed_values
        res = WrongTransaction.control(curr_from, curr_to, amount, name)
    except WrongTransaction as e:
        bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка сервера: {e}. Не удалось обработать запрос,если ошибка повторяется напишите нам - /report или проверте правильность написания команды /help ')
    else:
        text = f'Цена {amount} {keys[curr_from]} составляет: {res * Decimal(amount)} \n{keys[curr_to]}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
