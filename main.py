import discord
import os
from discord.ext import commands
from googletrans import Translator
from keep_alive import keep_alive
#intents = discord.Intents().all()
intents = discord.Intents.default()
intents.members = True
intents.message_content=True
client = commands.Bot(command_prefix=',', intents=intents)
#client = discord.Client(intents=)



@client.event

async def on_ready():
    print('{0.user} is ready!'.format(client))
  
@client.event
async def on_message(message):
    t = Translator()
    if message.author == client.user:
        return
    if message.content.startswith('$en'):
        await message.channel.send(t.translate(message.content.strip('$en'),dest='en').text)

keep_alive()
client.run('MTAwMjk2NTc0Nzg1MDU2MzY0NQ.GOg2y4.50w8hm0af9NxlSgkZHMfVQk9AWhnVUbGyW8f9w')