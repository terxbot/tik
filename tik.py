# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.6 (default, Jan 27 2021, 15:42:20) 
# [GCC 10.2.0]
# Embedded file name: TIKTOK BOT.py
# Compiled at: 2021-05-03 19:27:28
# Size of source mod 2**32: 4165 bytes
import telebot, requests, time, random
from telebot import types
import requests, random, datetime
from colorama import Fore

def error():
    while True:
        print('')
        print('نتهت مدة التجريبية')
        print('Error !! ')
        time.sleep(1000)


url = requests.get('https://pastebin.com/raw/B50EEXgt').text
if url == input('Enter user Activity:'):
    pass
else:
    error()
myadmin = input('id :')
q = input('TOKEN :')
N = 0
bot = telebot.TeleBot(q)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    iddu = str(message.from_user.id)
    if iddu in myadmin:
        nam = message.from_user.first_name
        mas = types.InlineKeyboardMarkup(row_width=1)
        D = types.InlineKeyboardButton('قناة المطور', url='https://t.me/EEIKG')
        mas.add(D)
        fg = bot.send_message((message.chat.id), f"هلا عزيزي المشترك “ {nam} ”\n\tفي بوت تشكير تيك توك\n\tاضغط لتشغيل “ /sta  ”", reply_markup=mas)
    else:
        mas = types.InlineKeyboardMarkup(row_width=1)
        A = types.InlineKeyboardButton('المطور', url='https://t.me/RKRKQ')
        C = types.InlineKeyboardButton('قناة المطور', url='https://t.me/EEIKG')
        mas.add(A, C)
        fg = bot.send_message((message.chat.id), '⚠️ || عذرا هاذة لبوت ليس مجاني قم بمراسلة المطور لتفعيل !!', reply_markup=mas)


@bot.message_handler(func=(lambda message: True))
def send_welcome(message):
    global ses
    global t
    i = 0
    if message.text == '/sta' or message.reply_to_message:
        if message.text == '/sta':
            bot.send_message(message.chat.id, '⌥ Enter SessionId')
        if message.reply_to_message:
            mes = message.reply_to_message.text
            if mes == '⌥ Enter SessionId':
                with open('sessionId.txt', 'w') as (x):
                    x.write(message.text)
                    bot.send_message(message.chat.id, 'Status done')
                    i = 1
    if i == 1:
        time.sleep(1.5)
        bot.send_message(message.chat.id, 'Number of username required')
    if message.reply_to_message:
        mes = message.reply_to_message.text
        if mes == 'Number of username required':
            try:
                t = int(message.text)
                mas = types.InlineKeyboardMarkup(row_width=2)
                A = types.InlineKeyboardButton('بدء', callback_data='F1')
                mas.add(A)
                ses = open('sessionId.txt', 'r').read().splitlines()
                fg = bot.send_message((message.chat.id), f"{t} \n {ses}", reply_markup=mas)
            except:
                bot.send_message(message.chat.id, '{t} \n {ses}')


@bot.callback_query_handler(func=(lambda call: True))
def sdd(call):
    if call.data == 'F1':
        bad = 0
        good = 0
        kol = 0
        error = 0
        payload = ''
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', 
         'Connection':'close', 
         'Host':'www.tiktok.com', 
         'Accept-Encoding':'gzip, deflate', 
         'Cache-Control':'max-age=0'}
        tuks1 = 'poiuytrewqasdfghjklmnbvcxz12'
        sess = open('sessionId.txt', 'r').read()
        for y in range(t):
            kol += 1
            ruks = str(''.join((random.choice(tuks1) for i in range(4))))
            url = 'https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=' + ruks + '&app_language=ar'
            cookies = {'sessionid': sess}
            r = requests.request('GET', url, data=payload, headers=headers, cookies=cookies)
            print(r.json())
            try:
                post = str(r.json()['status_msg'])
                if post == '':
                    timee = time.asctime()
                    good += 1
                    bot.send_message(call.message.chat.id, f"USER TIKTOK ✪\n\n≋ user : {ruks}\n\n≋ {timee}")
                else:
                    bad += 1
            except:
                error += 1
            else:
                bot.edit_message_text(chat_id=(call.message.chat.id), message_id=(call.message.message_id), text=f"STARTED ▶️\n\n🆔 ⋮ [{sess}]\n\n≋ Required number ⋮ {t}\n\n≋ \u2066∼❃∼User ⋮ {ruks}\n≋ \u2066∼✓∼ Done ⋮ {good}\n≋ \u2066∼✘∼Bad ⋮ {bad}\n≋ \u2066∼✘∼Error ⋮ {error}\n\n≋ Users ⋮ {kol}")


if __name__ == '__main__':
    bot.polling(none_stop=True)
# okay decompiling T2.pyc
