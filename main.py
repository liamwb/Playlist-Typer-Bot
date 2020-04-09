"""
Playlist-Typer-Bot, by Liam Wood-Baker, 2020.
This bot listens for someone who wants to queue a spotify playlist in a chat with Rhythm in it, and
writes the commands for each song in the playlist in to the chat.
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


playlistTest = spotify.playlist(playlist_id='https://open.spotify.com/playlist/5KfPRv6ynvPD2VwfD4y7ni?si=f6B4-7FURgSlbr-hSZTT7g')
print(json.dumps(playlistTest, indent=4))

# the bot proper begins. Authorisation for the discord bot happens at the end with bot.run(discordToken)
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='QueuePlaylist')
async def QueuePlaylist(url):
    await url.channel.send("it works")


bot.run(discordToken)
