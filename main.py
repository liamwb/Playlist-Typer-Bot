"""
Playlist-Typer-Bot, by Liam Wood-Baker, 2020.
This bot listens for someone who wants to queue a spotify playlist in a chat with Rhythm in it, and
writes the commands for each song in the playlist in to the chat.

This bot does not, in fact, work. Rythm does not listen to other bots
"""

import spotipy.oauth2 as oauth2
import spotipy
import json
import discord
from discord.ext import commands

# these are secret tokens, which you will need to create in the same location as this file
discordToken = open('DISCORD-TOKEN.txt').read()
clientSecret = open('SPOTIFY-CLIENT-SECRET.txt').read()

# getting authorisation for spotify
credentials = oauth2.SpotifyClientCredentials(
    client_id='b9a5c48552a84a5fb7a47acea0d2d9fc',
    client_secret=clientSecret)

spotifyToken = credentials.get_access_token()
spotify = spotipy.Spotify(auth=spotifyToken)

playlistTest = spotify.playlist(
    playlist_id='https://open.spotify.com/playlist/5KfPRv6ynvPD2VwfD4y7ni?si=f6B4-7FURgSlbr-hSZTT7g')

# the bot proper begins. Authorisation for the discord bot happens at the end with bot.run(discordToken)
bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='summon')
async def summon(ctx):
    # If summon is not called from a voice channel, then the bot doesn't know which one to join, so it doesn't
    if not ctx.author.voice:
        await ctx.send('You\'re not in a voice channel. \nYou\'re a big fuckhead.')
    else:
        channel = ctx.author.voice.channel
        await channel.connect()

# the whole point of this bot
@bot.command(name='queuePlaylist')
async def queuePlaylist(ctx, url: str):
    playlist = spotify.playlist(playlist_id=url)
    # playlist is a dict. We can find the info we want by navigating through 'tracks', and then 'items'
    for i in playlist['tracks']['items']:
        # if a track has multiple artists we're just looking at the first one
        artist = i['track']['artists'][0]['name']
        song = i['track']['name']
        await ctx.send('!play' + ' ' + song + ' ' + artist)



bot.run(discordToken)
