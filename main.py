import os
import discord
from discord.ext import commands
# from dotenv import load_dotenv

token = 'Njk3NjEzMTc5MzIwMTM5ODQ2.Xo55oQ.Os4lfdobuEo6sf2JCm46wSlGfoE'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='QueuePlaylist')
async def QueuePlaylist(url):
    await url.channel.send("it works")


bot.run(token)
