import telebot
import random

token = TOKEN_TG

helloNew = ["AwADAgADcQQAAoREaEna38mVwAQFUAI","AwADAgADSQUAAl-uYEnfeal9RBCGTwI","AwADAgADUgMAAoDgaEmL_YJE9ZIbJgI","AwADAgADUwMAAoDgaEkNTnUo3FC-kAI","AwADAgADKAUAAiR2aEmJLCMrfNQK8gI","AwADAgADRgMAAgfAaEmWyuNUpVtvEQI"]
 #AwADAgADLAQAAicSaUlvogAB8Y6wZjoC ой да  ладно тебе, мы же хорошие, ня!
Hello = ["AwADAgADRwMAAgfAaEliw-kNF6wJMgI"]
Bi = ["AwADAgAD4QIAAkXiaUldUVt0cRJyvwI"]

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
#Болталка
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_voice(message.chat.id, voice=(Hello[0]) )
        
    elif message.text =='Пока' :
        bot.send_voice(message.chat.id, voice=(Bi[0]) )
        
    
        
#приветствие новых пользователей
@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    bot.send_voice(message.chat.id, voice=(helloNew[random.randint(0,5)]) )
    
bot.polling()
