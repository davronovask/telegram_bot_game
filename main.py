import random
import telebot
from local_setting import API_TOKEN



bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в 'камень, ножницы, бумага'"
                          ".Выберите камень (к), ножницы (н) или бумагу (б)")


@bot.message_handler(func=lambda message: True)
def play_game(message):
    text = message.text
    text = text.lower()


    if text not in ["к", "н", "б"]:
        bot.reply_to(message, "Введите пожалуйста к, н или б")
    else:
        computer_move = random.choice(["к", "н", "б"])
        print("user", text)
        print("comp", computer_move)
        if text == "к" and computer_move == "н":
            bot.reply_to(message, "Вы выиграли")
        elif text == "н" and computer_move == "б":
            bot.reply_to(message, "Вы выиграли")
        elif text == "б" and computer_move == "к":
            bot.reply_to(message, "Вы выиграли")
        elif text == computer_move:
            bot.reply_to(message, "ничья!")
        else:
            bot.reply_to(message, "ВЫ ПРОИГРАЛИ!")


bot.infinity_polling()



