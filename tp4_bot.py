from discord.ext import commands
#from discord import Client
import discord
from datetime import datetime
import os


from dotenv import load_dotenv
load_dotenv(dotenv_path="config")


import logging
logging.basicConfig(filename='fichier_log.log', encoding='utf-8', level=logging.DEBUG)
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')




class MyBot(commands.Bot):
    

   # async def on_ready(self):
   #a     self.log.infolog(f"{self.user} has connected to Discord!")

    # Créer un événement
    async def on_ready(self):
        print("Le bot est prêt !")
        time = str(datetime.now())
        f = open("fichier_log.log", "a")
        f.write(time +"Le bot est prêt \n")
        f.close()


    async def on_message(ctx,message):
        if message.content == "Je suis perdue":
           await message.channel.send("J'arrive pas a faire la suite")
           time = str(datetime.now())
           f = open("fichier_log.log", "a")
           f.write(time + " Commande perdue utilisée \n")
           f.close()

        if message.content == "!help":

            embed=discord.Embed(title="Commandes additionnelles", color=0x553adf)
            embed.set_author(name="Le bébé bot de Sandra")
           # embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/3/38/Info_Simple.svg%22")
            embed.add_field(name="Je suis perdue", value="J'arrive pas a faire la suite", inline=False)
            embed.add_field(name="!where", value="salut!", inline=False)
            embed.add_field(name="!PHOTO", value="envoie une photo du bot", inline=False)
            await message.channel.send(embed=embed)

        
        if message.content =="!PHOTO":
            await message.channel.send("Voici une photo de moi!! {0.author.mention}".format(message),file=discord.File('super_bot.jpeg'))
            time = str(datetime.now())
            f = open("fichier_log.log", "a")
            f.write(time + " La commande !PHOTO a ete utilisee ! \n")
            f.close()

        if message.content =="!where":
            await message.channel.send("Un serveur de test pour e codage de bot {0.author.mention}".format(message))
            time = str(datetime.now())
            f = open("fichier_log.log", "a")
            f.write(time + " La commande !where a ete utilisee ! \n")
            f.close()

            
            


    

    async def on_member_join(self, member):
        guild = member.guild
        print("Quelqu'un a rejoint")
        if guild.system_channel is not None:
            to_send = 'bienvenue {0.mention} sur le serveur {1.name}'.format(member, guild)
            await guild.system_channel.send(to_send)



    
    
  
"""  
bot = MyBot()
  
bot.run(os.getenv("TOKEN"))

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "!", description = "Bot de Sandra")
@bot.event
async def on_ready():
    print("Ready !")
@bot.command()
async def Bonjour(ctx):
    await ctx.send("Bonjour !")
@bot.command()
async def InfoServeur(ctx):
    serveur = ctx.guild

    nombreDeChainesTexte = len(serveur.text_channels)
    nombreDeChainesVocale = len(serveur.voice_channels)
    Description_du_serveur = serveur.description
    Nombre_de_personnes = serveur.member_count
    Nom_du_serveur = serveur.name
    message = f"Le serveur **{Nom_du_serveur}** contient *{Nombre_de_personnes}* personnes ! \n La description du serveur est {Description_du_serveur}. \nCe serveur possède {nombreDeChainesTexte} salons écrit et {nombreDeChainesVocale} salon vocaux."
    await ctx.send(message)

@bot.event
async def on_member_join(ctx, user):
    message = f"Ce server a été rejoint' par **{user}**."
    await ctx.send(message)

@bot.command()
async def b99(ctx):
    serveur = ctx.guild
    
    await ctx.send("no doubt no doubt no doubt no doubt  !")

client = discord.Client()

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

bot.run("OTU4Njk0MDkzNzg4MTg0NTc2.YkRDcw.CZSfxB-XsM3IpK0jyE5TaSSFmGA")
"""