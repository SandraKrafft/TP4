from discord.ext import commands
#from discord import Client
import discord
from datetime import datetime
import os
from tp4_bot import MyBot


from dotenv import load_dotenv
load_dotenv(dotenv_path="config")


import logging
def main():

    logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info('Started')
 
    logging.info('Finished')
    intents = discord.Intents.default()
    intents.presences = True
    intents.members = True
    bot = MyBot(command_prefix = "!", intents=intents)


    bot.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    main()