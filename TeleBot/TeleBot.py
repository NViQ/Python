import telebot
import TeleBot
import requests
from bs4 import BeautifulSoup
import urllib.request

bot = telebot.TeleBot('5428334254:AAEmoEX1qzCFjGYJwVeEaPukOAH5aSbV_ew')

@bot.message_handler(commands=['start'])

def start(message):
    mess = f' Привет <b><u> {message.from_user.first_name} {message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


def reyting(message):
    req = urllib.request.urlopen('https://mafiauniverse.org/Players')
    html = req.read()

    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('a', class_='fw-bold')

    mess = f' Tвой рейтинг: <b><u></u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')




bot.polling(none_stop=True)