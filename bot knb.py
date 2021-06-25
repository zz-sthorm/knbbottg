import telebot 
from telebot import types 
import random 
import config 
 
bot = telebot.TeleBot(config.TOKEN) 
 
#тут достаем id игроков из лога 
log_users = [] 
f = open("log.txt",'r', encoding="utf-8") 
data = f.read() 
data = data.split("\n") 
f.close() 
for i in range(len(data)): 
    if data[i]!='': 
        buf = data[i].split("id: ") 
        log_users.append(int(buf[1])) 
print(log_users) 
 
ishod = 3 #исход битвы 
 
@bot.message_handler(commands=['start']) 
def start_message(message): 
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    keyboard.row("Начать игру") 
    bot.send_message(message.chat.id, 'Для начала игры с ботом нажмите кнопку', reply_markup = keyboard) 
     
@bot.message_handler(content_types=["text"]) 
def start_message(message): 
    if message.from_user.id != 944170657: 
 
        #имя игрока 
        name = str(message.from_user.first_name) 
        #--ход компа-- 
        hod = random.randint(0,2) 
        knb=["🗿","✂","🧻"] 
        bot.send_message(message.chat.id, knb[hod]) 
        #------------- 
        #--тут запишем в лог если присоединился новый пользователь-- 
        if log_users.count(message.from_user.id)==0: 
            log_users.append(message.from_user.id) 
            f = open("log.txt",'a', encoding="utf-8") 
            f.write(name+" id: "+str(message.from_user.id)+"\n") 
            f.close() 
            bot.send_message(int(log_users[0]), f"к нам присоединился: \n{name} \n+1 игрок({len(log_users)})") 
            print(f"к нам присоединился: \n{name} \n+1 игрок({len(log_users)})")     
        print(log_users) 
        #------------------------------------------------------------ 
        print(name,message.from_user.id,message.text,"bot", hod,"users",len(log_users)) 
        #--созадем клаву-- 
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        keyboard.row("🗿","✂","🧻") 
        #--выесняем кто кого-- 
        if message.text == "Начать игру": 
            bot.send_message(message.chat.id, "Ходи", reply_markup = keyboard) 
        elif message.text == "🗿" and hod==0: 
            ishod=0 
        elif message.text == "🗿" and hod==1: 
            ishod=1 
        elif message.text == "🗿" and hod==2: 
            ishod=2 
        elif message.text == "✂" and hod==1: 
            ishod=0 
        elif message.text == "✂" and hod==2: 
            ishod=1 
        elif message.text == "✂" and hod==0: 
            ishod=2 
        elif message.text == "🧻" and hod==2: 
            ishod=0 
        elif message.text == "🧻" and hod==0: 
            ishod=1 
        elif message.text == "🧻" and hod==1: 
            ishod=2 
        #стикеры реакция на исход игры 
        stic=["CAACAgIAAxkBAAEBe5Fg1FnXaKnPz2t8GZuRyUiDcfOPzQACqg0AAuODiUjd0_CDy4ej6x8E", 
              "CAACAgIAAxkBAAEBe4tg1FnP7kjRuMh-o59gqr37xZo01AACaQwAAq5xAUhEAxLuEF4rpR8E", 
              "CAACAgIAAxkBAAEBe45g1FnWSa-KUn0OkUuLXKVvQI3ysAAC-AsAAqydAAFIkwFAkULAXYYfBA"] 
        bot.send_sticker(message.chat.id, stic[ishod], reply_markup = keyboard) 
        #выводим статистику 
        bot.send_message(message.chat.id, f"Уникальных игроков: {len(log_users)}") 
    else: 
        bot.send_message(message.chat.id, f"не шали") 
@bot.message_handler(content_types=["sticker"]) 
def handle_docs_audio(message): 
    # Получим ID Стикера 
    sticker_id = message.sticker.file_id 
    print(sticker_id) 
    
bot.polling()