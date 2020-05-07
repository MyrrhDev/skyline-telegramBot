# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler

import pickle
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import skyline as sk

identificadores = []


# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkylineBot! Buenas!")
    
def author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Mayra Pastor Valdivia mayra.pastor@est.fib.upc.edu")

def help_person(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Tengo los comandos: /start, /help, /lst, /clean , /save id , /load id")

#Voy a tener que guardarme los identificadores (variables) en un dicc y print aqui y en el sig. borrar
#mostra els identificadors definits i la seva corresponent àrea.
def lst(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Mi creadora es @ Mayra Pastor Valdivia")

#esborra tots els identificadors definits.
def clean_this(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Mi creadora es @ Mayra Pastor Valdivia")

#/save id: ha de guardar un skyline definit amb el nom id.sky.
def save_id(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Mi creadora es @ Mayra Pastor Valdivia")

#/load id: ha de carregar un skyline de l’arxiu id.sky.
def load_id(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Mi creadora es @ Mayra Pastor Valdivia")

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher






# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('help', help_person))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean_this))
dispatcher.add_handler(CommandHandler('save id', save_id))
dispatcher.add_handler(CommandHandler('load id', load_id))

# engega el bot
updater.start_polling()
