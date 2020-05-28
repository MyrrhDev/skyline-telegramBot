from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import pickle
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import skyline as sk

import random
import os

import sys
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
                             text="Mayra Pastor Valdivia mayra.pastor@est.fib.upc.edu")


# contestar con una lista de todas las posibles pedidos y una breve documentación sobre su propósito y uso.
def help_person(update, context):
    text = """Los comandos disponibles son: \n
    /author: escribe el nombre completo del autor del proyecto y su correo electrónico oficial de la facultad.\n
    /start: Inicia la conversacion con el bot\n
    /help: Información sobre los comandos\n
    /lst: muestra los identificadores definidos y su correspondiente área.\n
    /clean: borra todos los identificadores definidos.\n
    /save id: guarda un skyline definido con el nombre id.sky.\n
    /load id: carga un skyline del archivo id.sky."""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)


# muestra los identificadores definidos y su correspondiente área.
def lst(update, context):
    print('lst')
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
    print('clean')
    context.user_data['ts'].clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Los identificadores han sido borrados")


# /save id: debe guardar un skyline definido con el nombre id.sky.
def save_id(update, context):
    print('saving')
    print(context.args[0], type(context.args[0]))
    # recoger el Skyline de la ts
    sky_save = sk.find_symbol(context.args[0], context.user_data['ts'])
    # Si no existe:
    if sky_save is None:
        context.bot.send_message(chat_id=update.effective_chat.id, text="El id no existe, intentalo de nuevo")
    sk.save_sky(sky_save, context.args[0])
    context.bot.send_message(chat_id=update.effective_chat.id, text="El skyline ha sido guardado")


# /load id: debe cargar un skyline del archivo id.sky.
def load_id(update, context):
    print('loading')
    print(context.args[0], type(context.args[0]))
    try:
        new_sky = sk.load_sky(context.args[0])
    except (OSError, IOError) as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No hay un archivo de ese nombre")
    # Si existe, (sobre)excribo en:
    sk.update_symbols(context.args[0], context.user_data['ts'], new_sky)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Se ha cargado el archivo en la tabla de simbolos")


def draw_graph(update, context, skyline):
    print('drawing graph')
    m_file = "%d.png" % random.randint(1000000, 9999999)
    ax = plt.figure().gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    print('info: ', skyline.get_x_pos(), skyline.get_height(), skyline.get_width() )

    plt.bar(skyline.get_x_pos(), skyline.get_height(), width=skyline.get_width(), align='edge')
    plt.savefig(m_file, bbox_inches='tight')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(m_file, 'rb'))
    os.remove(m_file)
    text = "area: " + str(skyline.get_area()) + "\n" + "altura: " + str(skyline.get_max_height())
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def user_operation(update, context):
    try:
        # Crear nuevo skyline
        # if (xmin >= xmax):
        #    context.bot.send_message(chat_id=update.effective_chat.id, text="El minimo ha de ser menor que el maximo")
        #    raise TypeError("xmin >= xmax")
        # elif(height <= 0):
        #    context.bot.send_message(chat_id=update.effective_chat.id, text="El minimo ha de ser menor que el maximo")
        #    raise TypeError("height <= 0")

        # skylines compuestos:
        # puedo hacer un loop y asignando a un skyline object,
        # [(xmin, alçada, xmax), ...] ...[(1, 2, 3), (3, 4, 6)]
        # i = 0
        # while i < len(lista_skyline):
        #    par_sk = lista_skyline[i]  #(xmin, alçada, xmax)
        #    temp_sk = sk.Skyline()
        # text = update.message.text

        # print(len(context.user_data['ts']))
        # if not 'ts' in context.user_data:
        #    context.user_data['ts'] = dict()

        print('1')
        input_stream = InputStream(update.message.text)
        lexer = SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()
        # y luego usas una instancia de EvalVisitor para seguir...
        print('2')
        visitor = EvalVisitor(context.user_data['ts'])
        # donde context.user_data['ts'] es la tabla de símbolos
        # que el bot guarda para el usuario en cuestión...
        print('3')
        # m_output tendrá el skyline a plotear
        m_output = visitor.visit(tree)
        draw_graph(update, context, m_output)

    except Exception as e:
        print('Its going down: ')
        print(e, type(e))
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('help', help_person))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean_this))
# pass_args=True porque sera el 'id' ...pero acabo de leer que ya no es necesario y siempre se pasa todo y se puede usar.
dispatcher.add_handler(CommandHandler('save', save_id))
dispatcher.add_handler(CommandHandler('load', load_id))

# draw_graphs es la funcion
dispatcher.add_handler(MessageHandler(Filters.text, user_operation))

# engega el bot
updater.start_polling()
