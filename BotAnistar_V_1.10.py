import telebot

token = 'TOKEN_TG'

mas = ["AwADAgADcQQAAoREaEna38mVwAQFUAI","AwADAgADSQUAAl-uYEnfeal9RBCGTwI","AwADAgADUgMAAoDgaEmL_YJE9ZIbJgI","AwADAgADUwMAAoDgaEkNTnUo3FC-kAI","AwADAgADKAUAAiR2aEmJLCMrfNQK8gI"]
# AwADAgADLAQAAicSaUlvogAB8Y6wZjoC ой да  ладно тебе, мы же хорошие, ня!


bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
#Болталка
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Приветствую тебя мой повелитель');
        
    elif message.text =='Пока' :
        bot.send_message(message.chat.id, 'Я буду ждать вашего возвращения господин')
        
    
        
#приветствие новых пользователей
@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    bot.send_voice(message.chat.id, voice=(mas[1]) )
    
bot.polling()
