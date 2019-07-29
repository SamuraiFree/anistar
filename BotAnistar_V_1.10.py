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
"helloNewUsers/helloNewUsersA1.ogg",
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
"hello/hello_10.ogg",
"hello/hello_11.ogg",
"hello/hello_12.ogg",]
coll_Hello = len(Hello)-1


matt = ["endos/mat1.ogg",
"endos/mat2.ogg",
"endos/mat3.ogg",
"endos/mat4.ogg",
"endos/mat5.ogg",
"endos/mat6.ogg",
"endos/mat7.ogg",
"endos/mat8.ogg",
"endos/mat9.ogg",
"endos/mat10.ogg",
"endos/mat11.ogg",
"endos/mat12.ogg",
"endos/mat13.ogg",
"endos/mat14.ogg",
"endos/mat15.ogg",]
coll_matt = len(matt)-1



Bi = ["bi/bi_1.ogg",
"bi/bi_2.ogg",
"bi/bi_4.ogg",
"bi/bi_5.ogg",
"bi/bi_6.ogg",
"bi/bi_7.ogg",
"bi/bibi.ogg"]
coll_Bi = len(Bi)-1
#########Маты
bzzz=["хуй","Хуй","Хуйня","хуйня","блять","Блять","Бля","бля","Пидорас",
      "пидорас","Пидор","пидор","блядина","Блядина","хуйла","хуйло","Хуйло",
      "Нахуй","нахуй","мудила","Мудила","Пиздец","пиздец","ебанаврот","Ебанаврот",
      "Сука","сука","Сучара","сучара","Сукин",
      "сукин","сучка","Сучка","Соси","Соси","Пиздоблятское","пиздоблятское",
      "мудоебище","Мудоебище","хую","Хую","Мудаков","мудаков",
      "хуя","Хуя","Нихуя","нихуя","Пиздеж","пиздеж","Лох",
      "лох","Чмо","чмо","Заебался","заебался","пидр","Пидр","Еби","еби","Ебись",
      "Пидорасы","пидорасы","суки","Суки","Хуиглот","хуиглот","ебу","Ебу","Ебал",
      "ебал",
      "Жопа","жопа","Жопу","жопу","анус","Анус","Сучка","сучка","хули","Хули","блядство","Блядство",
      "Конченный","конченный","Анимевост","анимевост","Анилибрия","анилибрия","AnimeVost","animevost",
      "Анимевосторг","анимевосторг","Анивост","анивост","Либрия","либрия","Мартышлюшка","мартышлюшка","винда"]
#############
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
#Болталка
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        voice = open(Hello[random.randint(0,coll_Hello)], 'rb')
        bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
        
    elif message.text =='Пока' :
        voice = open(Bi[random.randint(0,coll_Bi)], 'rb')
        bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
        
    
    elif message.text =='Все идет по плану' :
        audio = open("helloNewUsers/VseIdetPoPlanu.mp3", 'rb')
        bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='Все идет по плану!' :
        audio = open("helloNewUsers/VseIdetPoPlanu.mp3", 'rb')
        bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='все идет по плану' :
        audio = open("helloNewUsers/VseIdetPoPlanu.mp3", 'rb')
        bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='все идет по плану!' :
        audio = open("helloNewUsers/VseIdetPoPlanu.mp3", 'rb')
        bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='Ели мясо мужики!' :
        audio = open("endos/eli.mp3", 'rb')
        bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='Ели мясо мужики' :
        audio = open("endos/eli.mp3", 'rb')
        bot.send_audio(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='Ты потрясающий' :
        voice = open("helloNewUsers/tiPotr.ogg", 'rb')
        bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
    elif message.text =='Ты потрясающий!' :
        voice = open("helloNewUsers/tiPotr.ogg", 'rb')
        bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
    elif message.text =='Чем занимаешься?' :
        voice = open("endos/nlo.ogg", 'rb')
        bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
    elif message.text =='чем занимаешься?' :
        voice = open("endos/nlo.ogg", 'rb')
        bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
    elif message.text =='Чем занимаешься' :
        voice = open("endos/nlo.ogg", 'rb')
        bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
    elif message.text =='чем занимаешься' :
        voice = open("endos/nlo.ogg", 'rb')
        bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
    elif message.text =='Расслабься' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='расслабься' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='Не волнуйся.' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='не волнуйся.' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='Не волнуйся' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='не волнуйся' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='Мир.' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='мир' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
     elif message.text =='Мир' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
    elif message.text =='мир.' :
        audio = open("endos/RastaDontWory.mp3", 'rb')
        bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)
      
      
    elif message.text =='Бот' :
        bot.send_message(message.chat.id, 'Ты кого ботом назвал? Порву как тузик грелку!!!',reply_to_message_id=message.message_id)
    elif message.text =='бот' :
        bot.send_message(message.chat.id, 'Ты кого ботом назвал? Порву как тузик грелку!!!',reply_to_message_id=message.message_id)
    else:
        a=message.text
        z=a.split()
        for i in z:
            for c in bzzz:
                if i == c:
                    voice = open(matt[random.randint(0,coll_matt)], 'rb')
                    bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
        
    
  
        
#приветствие новых пользователей
@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    voice = open(helloNew[random.randint(0,coll_helloNew)], 'rb')
    bot.send_voice(message.chat.id, voice, reply_to_message_id=message.message_id)
    
bot.polling()
