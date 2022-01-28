import discord
import os
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import datetime
import logging


bot = ChatBot(
    'GayBowser',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        user_input = message.content
        ai_input = user_input.replace('$', '')

        bot_response = bot.get_response(ai_input)

        print('Input: ' + str(ai_input))
        print('Output: ' + str(bot_response))
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f.write(str(current_time) + ' --> ' + str(message.author) + ':' +str(ai_input) + ' --> ' + str(bot_response) + '\n')
        await message.channel.send(str(bot_response))


#if os.path.exists('database.db') != True:
    #trainer()


f = open('log.txt', 'w+')
client.run('')

