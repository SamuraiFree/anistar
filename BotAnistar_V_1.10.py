import telebot
import random

token = "861985547:AAEN61AyePKOwwwcnYOPI6VLvwZDF6YpqEI"

helloNew = ["AwADAgAD5AMAAlS_eEmHHBqyfxYgbAI","AwADAgAD4QMAAlS_eEnSGj85-9fZHQI","AwADAgAD3gMAAo2OcUnyup0bUvh-TQI","AwADAgADvAUAAj0yeEmLMD0nHnbQKAI","AwADAgADvAUAAj0yeEmLMD0nHnbQKAI","AwADAgADxQMAAla-aUmWa4-NVHJ_7wI","AwADAgADyQMAAla-aUl5yt_f25SB2AI","AwADAgADoAQAAhxucElD4vRVuE4icQI","AwADAgADzAMAAla-aUkBM5bAy_uqJAI","AwADAgADAwQAAt0RcUm96BlMFQQjSQI","AwADAgADXgMAAq-hcUkpSWEBmd3r_gI","AwADAgADUgQAAs01aElBrpp-LSqJPAI"]
#AwADAgADLAQAAicSaUlvogAB8Y6wZjoC ой да  ладно тебе, мы же хорошие, ня!
Hello = ["AwADAgADHwQAAt0RcUk4NdltrWzuOwI","AwADAgAD4QMAAlS_eEnSGj85-9fZHQI","AwADAgAD5AMAAlS_eEmHHBqyfxYgbAI","AwADAgADWQQAAlS_eEn-ZG_pwyrU3QI","AwADAgADWgQAAlS_eEnd3oyrVnjjMgI","AwADAgADXgQAAlS_eEnOKmcT9z2xAAEC","AwADAgADlAQAAvOkeEkAAVziIkZhFU4C","AwADAgADYQQAAlS_eEkX1_BGj_Y68wI","AwADAgADlQQAAvOkeEll1hwtQqib5gI","AwADAgADYgQAAlS_eEkUnef00soWcAI","AwADAgADlgQAAvOkeEmfC3R7K2lPjwI"]
Bi = ["AwADAgAD4QIAAkXiaUldUVt0cRJyvwI"]

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
#Болталка
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_voice(message.chat.id, voice=(Hello[random.randint(0,(len(Hello)-1))]) )
        
    elif message.text =='Пока' :
        bot.send_voice(message.chat.id, voice=(Bi[0]) )
        
    
        
#приветствие новых пользователей
@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    bot.send_voice(message.chat.id, voice=(helloNew[random.randint(0,(len(helloNew)-1))]) )
    
bot.polling()
