import telebot
import random


token = "861985547:AAEN61AyePKOwwwcnYOPI6VLvwZDF6YpqEI"

helloNew = ["AwADAgADlgQAApwvgEml69nLGGt5uwI","AwADAgAD5AMAAlS_eEmHHBqyfxYgbAI","AwADAgAD4QMAAlS_eEnSGj85-9fZHQI","AwADAgAD3gMAAo2OcUnyup0bUvh-TQI","AwADAgADvAUAAj0yeEmLMD0nHnbQKAI","AwADAgADvAUAAj0yeEmLMD0nHnbQKAI","AwADAgADxQMAAla-aUmWa4-NVHJ_7wI","AwADAgADyQMAAla-aUl5yt_f25SB2AI","AwADAgADoAQAAhxucElD4vRVuE4icQI","AwADAgADzAMAAla-aUkBM5bAy_uqJAI","AwADAgADAwQAAt0RcUm96BlMFQQjSQI","AwADAgADXgMAAq-hcUkpSWEBmd3r_gI","AwADAgADUgQAAs01aElBrpp-LSqJPAI"]
coll_helloNew = len(helloNew)-1



Hello = ["AwADAgADGQYAAtw_iUl70atLjneUFAI","AwADAgADHwQAAt0RcUk4NdltrWzuOwI","AwADAgADWQQAAlS_eEn-ZG_pwyrU3QI","AwADAgADWgQAAlS_eEnd3oyrVnjjMgI","AwADAgADXgQAAlS_eEnOKmcT9z2xAAEC","AwADAgADlAQAAvOkeEkAAVziIkZhFU4C","AwADAgADYQQAAlS_eEkX1_BGj_Y68wI","AwADAgADlQQAAvOkeEll1hwtQqib5gI","AwADAgADYgQAAlS_eEkUnef00soWcAI","AwADAgADlgQAAvOkeEmfC3R7K2lPjwI"]
coll_Hello = len(Hello)-1



Bi = ["AwADAgADGgYAAtw_iUmOrywYfFen7QI"]

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
#Болталка
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_voice(message.chat.id, voice=(Hello[random.randint(0,coll_Hello)]) )
        
    elif message.text =='Пока' :
        bot.send_voice(message.chat.id, voice=(Bi[0]) )
        
    elif message.text == 'Ты потрясающий':
        bot.send_voice(message.chat.id, voice=("AwADAgADWQMAAkXJiEluk4EIWK8fCQI") )
        
    elif message.text =='ты потрясающий' :
        bot.send_voice(message.chat.id, voice=("AwADAgADWQMAAkXJiEluk4EIWK8fCQI") )

    elif message.text =='Доброе утро' :
        bot.send_voice(message.chat.id, voice=("AwADAgAD4wMAAjtqgUmAQWmf8wzDkgI") )

    elif message.text =='доброе утро' :
        bot.send_voice(message.chat.id, voice=("AwADAgAD4wMAAjtqgUmAQWmf8wzDkgI") )

    elif message.text =='Как дела?' :
        bot.send_voice(message.chat.id, voice=("AwADAgAD8wMAAjtugUmROyK_KjnQgAI") )
    elif message.text =='как дела?' :
        bot.send_voice(message.chat.id, voice=("AwADAgAD8wMAAjtugUmROyK_KjnQgAI") )
    elif message.text =='Чем занимаешься?' :
        bot.send_voice(message.chat.id, voice=("AwADAgADtgQAAt0ngEmxec0aQanmoAI") )
    elif message.text =='чем занимаешься?' :
        bot.send_voice(message.chat.id, voice=("AwADAgADtgQAAt0ngEmxec0aQanmoAI") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    elif message.text =='#' :
        bot.send_voice(message.chat.id, voice=("№") )
    
        
    
        
#приветствие новых пользователей
@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    bot.send_voice(message.chat.id, voice=(helloNew[random.randint(0,coll_helloNew)]) )
    
bot.polling()
