from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import pickle
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from skyline import Skyline as sk

import random
import os

from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor


# define una función que saluda y que se ejecutará cuando el bot reciba el mensaje/start
def start(update, context):
    if not 'ts' in context.user_data:
        context.user_data['ts'] = dict()
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkylineBot! Hola!")


# escribe el nombre completo del autor del proyecto y su correo electrónico oficial de la facultad.
def author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Mayra Pastor Valdivia, 2020\n"
                                  "mayra.pastor@est.fib.upc.edu")


# contestar con una lista de todas las posibles pedidos y una breve documentación sobre su propósito y uso.
def help_person(update, context):
    text = """Los comandos disponibles son: \n
    /start: Inicia la conversacion con el bot\n
    /author: escribe el nombre completo del autor del proyecto y su correo electrónico oficial de la facultad.\n    
    /lst: muestra los identificadores definidos y su correspondiente área.\n
    /clean: borra todos los identificadores definidos.\n
    /save id: guarda un skyline definido con el nombre id.sky.\n
    /load id: carga un skyline del archivo id.sky.\n
    /help: Información sobre los comandos"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)


# muestra los identificadores definidos y su correspondiente área.
def lst(update, context):
    identifier_dict = context.user_data['ts']
    m_areas = ""
    for key, value in identifier_dict.items():
        m_areas = m_areas + key + ': area ' + str(value.get_area()) + '\n'
    # Si no hay ningun identificador en la ts
    if m_areas == "":
        m_areas = "No hay identificadores"
    context.bot.send_message(chat_id=update.effective_chat.id, text=m_areas)


# borra todos los identificadores definidos.
def clean_this(update, context):
    context.user_data['ts'].clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Los identificadores han sido borrados")


# /save id: debe guardar un skyline definido con el nombre id.sky.
def save_id(update, context):
    print('saving')
    # recoger el Skyline de la ts
    sky_save = sk.find_symbol(context.args[0], context.user_data['ts'])
    # Si no existe:
    if sky_save is None:
        context.bot.send_message(chat_id=update.effective_chat.id, text="El id no existe, intentalo de nuevo")
    try:
        with open(context.args[0] + '.sky', 'wb') as user_file:
            pickle.dump(sky_save, user_file)
            print('saved')
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))
    context.bot.send_message(chat_id=update.effective_chat.id, text="El skyline ha sido guardado")


# /load id: debe cargar un skyline del archivo id.sky.
def load_id(update, context):
    up_sky = sk(0,0,0)
    try:
        with open(context.args[0] + '.sky', 'rb') as n_sky:
            up_sky = pickle.load(n_sky)
    except (OSError, IOError) as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No hay un archivo de ese nombre")
    # Si existe, (sobre)excribo en:
    try:
        context.user_data['ts'] = sk.update_symbols(context.args[0], context.user_data['ts'], up_sky)
        print('updated')
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Se ha cargado el archivo en la tabla de simbolos")


def draw_graph(update, context, skyline):
    m_file = "%d.png" % random.randint(1000000, 9999999)
    ax = plt.figure().gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.bar(skyline.get_x_pos(), skyline.get_height(), width=skyline.get_width(), align='edge', color='red')
    plt.savefig(m_file, bbox_inches='tight')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(m_file, 'rb'))
    os.remove(m_file)
    text = "area: " + str(skyline.get_area()) + "\n" + "altura: " + str(skyline.get_max_height())
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def user_operation(update, context):
    try:
        input_stream = InputStream(update.message.text)
        lexer = SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()
        visitor = EvalVisitor(context.user_data['ts'])
        m_output = visitor.visit(tree)
        draw_graph(update, context, m_output)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('help', help_person))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean_this))
dispatcher.add_handler(CommandHandler('save', save_id))
dispatcher.add_handler(CommandHandler('load', load_id))
dispatcher.add_handler(MessageHandler(Filters.text, user_operation))

# el bot
updater.start_polling()
