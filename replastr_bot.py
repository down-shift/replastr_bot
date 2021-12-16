import telebot
from random import randint

token = ''

bot = telebot.TeleBot(token)

# button markup

markup = telebot.types.ReplyKeyboardMarkup(row_width = 2)
btn1 = telebot.types.KeyboardButton('Вернуться')
btn2 = telebot.types.KeyboardButton('Пожертвовать команде')
markup.add(btn1, btn2)

# replies
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Загрузи фотографию бутылки, и нейросеть определит тип пластика, из которого она сделана.')
    bot.send_message(message.chat.id, 'Фотографию желательно делать лицевой стороной к бутылке.')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вернуться")

@bot.message_handler(content_types = ['text'])
def text(message):
    pl_kinds = ['PET', 'HDPE', 'PVC']
    if message.text.lower() == 'вернуться':
        try:
            markup = telebot.types.ReplyKeyboardRemove(selective=False)
        finally:
            bot.send_message(message.chat.id, 'Бот готов принять фотографию бутылки на анализ.', reply_markup = markup)
    if message.text.lower() == 'пожертвовать команде':
        try:
            markup = telebot.types.ReplyKeyboardRemove(selective=False)
        finally:
            bot.send_message(message.chat.id, 'Данная функция пока находится в разработке.', reply_markup = markup)
            bot.send_message(message.chat.id, 'Бот готов принять фотографию бутылки на анализ.', reply_markup = markup)
            # return to start screen

@bot.message_handler(content_types = ['photo'])
def photo_handling(message):
    # processing image
    cnt = 0
    pl_kinds = ['PET', 'HDPE', 'PVC', 'LDPE', 'PP', 'PS', 'O']
    tm_kinds = ['Sprite', 'Чудо']
    main_type = 0
    label_type = 0
    lid_type = 0
    trademark = ''
    address = 'Песочная ул., 10'
    bot.send_message(message.chat.id, 'Фотография получена, приступаем к анализу.')
    cnt = randint(1, 3)
    if cnt % 2 == 0: 
        main_type = 1
        lid_type = 2
        label_type = 3
    else:
        main_type = 2
        lid_type = 2
        label_type = 3
    trademark = tm_kinds[cnt%2]
    # define main_type and str_main_type
    msg1 = 'Марка бутылки: ' + trademark
    bot.send_message(message.chat.id, msg1)
    # a very long string  
    msg2 = 'Тип пластика : ' + str(main_type) + ' / ' + pl_kinds[main_type - 1] + ', тип пластика крышки: ' # 'Тип пластика : ' + str(main_type) + ' / ' + pl_kinds[main_type] + ', тип пластика крышки: '
    msg2 += str(lid_type) + ' / ' + pl_kinds[lid_type - 1] + ' , тип пластика этикетки: ' + str(label_type) + ' / ' + pl_kinds[label_type - 1] # str(lid_type) + ' / ' + pl_kinds[lid_type] + ' , тип пластика этикетки: ' + str(label_type) + ' / ' + pl_kinds[label_type]
    msg3 = 'Ближайший пункт переработки: ' + address
    bot.send_message(message.chat.id, msg2)
    bot.send_message(message.chat.id, msg3)
    if main_type == 3 or lid_type == 3 or label_type == 3:
        bot.send_message(message.chat.id, 'Внимание! Пластик типа 3 / PVC нельзя утилизировать.')
    if main_type == 7 or lid_type == 7 or label_type == 7 :
        bot.send_message(message.chat.id, 'Внимание! Пластик типа 7 / O нельзя утилизировать.')
        
    some_str = 'Нажми «Вернуться», чтобы ещё раз загрузить фотографию для анализа. Нажми «Узнать больше», чтобы получить дополнительные рекомендации по утилизации.'
    bot.send_message(message.chat.id, some_str, reply_markup = markup)

    cnt += 1

bot.polling(none_stop = True)

