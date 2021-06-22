import telebot

token = '1839701570:AAFWyy4v8semlyErEDSaM5EqKuYvQGAeJQY'

bot = telebot.TeleBot(token)

# button markup
markup = telebot.types.ReplyKeyboardMarkup(row_width = 2)
btn1 = telebot.types.KeyboardButton('Вернуться')
btn2 = telebot.types.KeyboardButton('Узнать больше')
markup.add(btn1, btn2)

# replies
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Загрузи фотографию бутылки, и нейросеть определит тип пластика, из которого она сделана.')
    bot.send_message(message.chat.id, 'Фотографию желательно делать лицевой стороной к бутылке.')

@bot.message_handler(content_types = ['text'])
def text(message):
    if message.text.lower() == 'вернуться':
        try:
            markup = telebot.types.ReplyKeyboardRemove(selective=False)
        finally:
            bot.send_message(message.chat.id, 'Бот готов принять фотографию бутылки на анализ.', reply_markup = markup)
    if message.text.lower() == 'узнать больше':
        try:
            markup = telebot.types.ReplyKeyboardRemove(selective=False)
        finally:
            if pl_type == 1:
                bot.send_message(message.chat.id, 'Рекомендации по PET', reply_markup = markup)
            if pl_type == 2:
                bot.send_message(message.chat.id, 'Рекомендации по HDPE', reply_markup = markup)
            if pl_type == 3:
                bot.send_message(message.chat.id, 'Рекомендации по PVC', reply_markup = markup)
            
            # return to start screen

pl_kinds = ['PET', 'HDPE', 'PVC']
tm_kinds = ['Sprite', 'Чудо']
count = 0
main_type = 0
label_type = 0
lid_type = 0
trademark = ''
address = 'Песочная ул., 10'

@bot.message_handler(content_types = ['photo'])
def photo_handling(message):
    # processing image
    bot.send_message(message.chat.id, 'Фотография получена, приступаем к анализу.')

    if count % 2 == 0:
        main_type = 1
        lid_type = 2
        label_type = 3
    else:
        main_type = 2
        lid_type = 2
        label_type = 3

    # define main_type and str_main_type
    msg1 = 'Марка бутылки: ' + trademark
    # a very long string  
    msg2 = 'Тип пластика : ' + str(main_type) + ' / ' + pl_kinds[main_type - 1] + ', тип пластика крышки: ' + str(lid_type) + ' / ' + pl_kinds[lid_type - 1] + ' , тип пластика этикетки: ' + str(label_type) + ' / ' + pl_kinds[label_type]
    msg3 = 'Ближайший пункт переработки: ' + address
    bot.send_message(message.chat.id, msg1)
    bot.send_message(message.chat.id, msg2)
    bot.send_message(message.chat.id, msg3)

    bot.send_message(message.chat.id, 'Нажми «Вернуться», чтобы ещё раз загрузить фотографию для анализа. Нажми «Узнать больше», чтобы получить дополнительные рекомендации по утилизации.', reply_markup = markup)


    count += 1

bot.polling()
