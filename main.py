import spotipy.oauth2 as oauth2
import spotipy
import discord
from discord.ext import commands

discordToken = open('DISCORD-TOKEN.txt').read()


clientSecret = open('SPOTIFY-CLIENT-SECRET.txt').read()

credentials = oauth2.SpotifyClientCredentials(
        client_id='b9a5c48552a84a5fb7a47acea0d2d9fc',
        client_secret=clientSecret)

spotifyToken = credentials.get_access_token()
spotify = spotipy.Spotify(auth=spotifyToken)

print(spotify.playlist(playlist_id='https://open.spotify.com/playlist/5KfPRv6ynvPD2VwfD4y7ni?si=f6B4-7FURgSlbr-hSZTT7g'))



bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='QueuePlaylist')
async def QueuePlaylist(url):
    await url.channel.send("it works")


bot.run(discordToken)
