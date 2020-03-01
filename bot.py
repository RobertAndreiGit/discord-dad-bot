import discord
import requests
from discord.ext import commands

client = commands.Bot(command_prefix = '--')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author.bot:
        return;

    channel = message.channel

    if message.content.startswith('!dadjoke'):
        response = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'text/plain'})
        await channel.send(response.text);

    words = message.content.split();

    for idx,word in enumerate(words):
        lwrcase = word.lower();
        if lwrcase == "i'm" or lwrcase == "im" or lwrcase == 'sunt':
            await channel.send('Hi ' + words[idx+1] + ", I'm Dad!");
        if lwrcase == 'i' and (words[idx+1] == 'am'):
            await channel.send('Hi ' + words[idx+2] + ", I'm Dad!");

client.run('DISCORD BOT TOKEN GOES HERE')
