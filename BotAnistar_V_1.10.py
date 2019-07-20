import telebot
import random


token = "861985547:AAEN61AyePKOwwwcnYOPI6VLvwZDF6YpqEI"


helloNew = ["helloNewUsers/helloNewUsers_1.ogg",
"helloNewUsers/helloNewUsers_2.ogg",
"helloNewUsers/helloNewUsers_3.ogg",
"helloNewUsers/helloNewUsers_4.ogg",
"helloNewUsers/helloNewUsers_5.ogg",
"helloNewUsers/helloNewUsers_6.ogg",
"helloNewUsers/helloNewUsers_7.ogg",
"helloNewUsers/helloNewUsers_8.ogg",
"helloNewUsers/helloNewUsers_9.ogg",
"helloNewUsers/helloNewUsers_10.ogg",
"helloNewUsers/helloNewUsers_11.ogg",
"helloNewUsers/helloNewUsers_12.ogg",]
coll_helloNew = len(helloNew)-1



Hello = ["hello/hello_1.ogg",
"hello/hello_2.ogg",
"hello/hello_3.ogg",
"hello/hello_4.ogg",
"hello/hello_5.ogg",
"hello/hello_6.ogg",
"hello/hello_7.ogg",
"hello/hello_8.ogg",
"hello/hello_9.ogg",
"hello/hello_10.ogg",
"hello/hello_11.ogg",]
coll_Hello = len(Hello)-1



Bi = ["bi/bi_1.ogg",
"bi/bi_2.ogg",
"bi/bi_3.ogg",
"bi/bi_4.ogg",
"bi/bi_5.ogg",
"bi/bi_6.ogg",
"bi/bi_7.ogg"]
coll_Bi = len(Bi)-1

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
#Болталка
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        voice = open(Hello[random.randint(0,coll_Hello)], 'rb')
        bot.send_voice(message.chat.id, voice)
        
    elif message.text =='Пока' :
        voice = open(Bi[random.randint(0,coll_Bi)], 'rb')
        bot.send_voice(message.chat.id, voice)
        
    
  
        
#приветствие новых пользователей
@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    voice = open(helloNew[random.randint(0,coll_helloNew)], 'rb')
    bot.send_voice(message.chat.id, voice)
    
bot.polling()
