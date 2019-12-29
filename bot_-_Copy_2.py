import discord
import random
import youtube_dl
import os
from discord.ext import commands


client = commands.Bot(command_prefix= '!')

players = {}

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the poophole.')

@client.event
async def on_member_remove(member):
    print(f'{member} has ascended from the depths of hell.')

@client.command(aliases=['Poop','poop'])
async def bernie(ctx):
    await ctx.send('poop')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def play(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = voice_client.play(discord.FFmpegPCMAudio(random.choice(os.listdir("./Music")))) #grabs filename just fine. Needs variable to be full path
    player.start()

    await channel.disconnect()



client.run('Hidden')
