from imap_tools import MailBox, AND
from mytoken import PassXablau, TeleToken
from gtts import gTTS
import time, telebot

bot = telebot.TeleBot(TeleToken())
print('Connected!!!')

user = 'YOUR_EMAIL'
passwd = PassXablau()

@bot.message_handler(commands=['start'])
def AlertEmail(message):
    bot.reply_to(message, 'Monitoring of new active emails!')
    while True:
        with MailBox('imap.gmail.com').login(user, passwd) as inbox:
            for msg in inbox.fetch(AND(seen=False)):
                alert = 'email.mp3'
                gtts = gTTS(
                    text=f'New email from {msg.from_}',
                    lang='pt-br'
                )
                gtts.save(alert)
                bot.send_voice(message.chat.id, open(f'{alert}', 'rb'))
                time.sleep(1)

bot.infinity_polling()
