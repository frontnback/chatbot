from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('./chatterbot-corpus/chatterbot_corpus/data/english')
    data = open('./chatterbot-corpus/chatterbot_corpus/data/english')
    bot.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot :',reply)
    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break
