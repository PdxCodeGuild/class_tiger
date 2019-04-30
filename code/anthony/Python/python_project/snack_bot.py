import discord
from discord.ext import commands
import time
import asyncio
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import random



client = discord.Client()
token = open('token.txt', 'r').read()
snackbox = 145416058554155008

def server_report(server):
    online = 0
    idle = 0
    offline = 0
    for i in server.members:
        if str(i.status) == 'online':
            online += 1
        if str(i.status) == 'offline':
            offline += 1
        else:
            idle += 1
    return online, idle, offline

async def server_metrics():
    await client.wait_until_ready()

    server = client.get_guild(snackbox)
    while not client.is_closed():
        try:
            online, idle, offline = server_report(server)
            with open("servermetrics.csv","a") as f:
                f.write(f"{int(time.time())},{online},{idle},{offline}\n")
            
            plt.clf()
            df = pd.read_csv("servermetrics.csv", names=['time', 'online', 'idle', 'offline'])
            df['date'] = pd.to_datetime(df['time'],unit='s')
            df['total'] = df['online'] + df['offline'] + df['idle']
            df.drop('time', 1, inplace = True)
            df.set_index('date', inplace = True)
            df['online'].plot()
            plt.legend()
            plt.savefig('online.png')
            
            await asyncio.sleep(3600)
        except Exception as e:
            print(str(e))
            await asyncio.sleep(3600)

def game_list(server):
    games = []
    for member in server.members:
        if member.activity == None:
            pass
        elif member.activity!=None:
            game = member.activity.name
            games.append(game)
    return games


def game_played(server):
    games = {}
    for member in server.members:
        if member.activity != None:
            game = member.activity.name
            if game not in games:
                games[game] = 1
            else:
                games[game] += 1
    return games

async def game_tracker():
    await client.wait_until_ready()
    server = client.get_guild(snackbox)
    while not client.is_closed():
        playing = game_played(server)
        with open("game_tracker.csv", 'a') as f:
            for game in playing:
                f.write(f"{game},{playing[game]}\n")
        plt.clf()
        df = pd.read_csv("game_tracker.csv", names=['Title', 'Hours'])
        df = df.groupby(['Title']).sum()
        df.plot(kind='barh', alpha=.7)
        plt.tick_params(axis='y', pad=-200)
        plt.legend()
        plt.savefig('hours_played.png')
        # await client.get_channel(570748812331843585).send(f"{playing}")
        await asyncio.sleep(3600)



@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    game = discord.Activity(name='Avengers: End Game', type=discord.ActivityType.watching)
    await client.change_presence(activity=game)



@client.event
async def on_message(message):
    server = client.get_guild(snackbox)
    if "!hello" in message.content.lower():
        await message.channel.send(f'Hello {message.author.name}')
    if "!hug" in message.content.lower():
        await message.channel.send(f'*{client.user.name} hugs {message.author.mention}*')
    if "!online" in message.content.lower():
        online, idle, offline = server_report(server)
        await message.channel.send(f"```{server.member_count} Members. \nOnline: {online}. \nIdle/busy/dnd: {idle}. \nOffline: {offline}.```")
        file = discord.File('online.png', filename='online.png')
        await message.channel.send(file=file)
    if "!time_played" in message.content.lower():
        file = discord.File('hours_played.png', filename='hours_played.png')
        await message.channel.send(file=file)
    if "!snackbot_logout" in message.content.lower():
        await client.close()
    if "!snackbox" in message.content.lower():
        await message.channel.send("||is just a box of snacks||")
    if "!snackbot" in message.content.lower():
        magic_ball = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
        answer = random.choice(magic_ball)
        await message.channel.send(f"```{answer}```")
    if "game_list" in message.content.lower():
        games = ''
        games_list = []
        games_list = game_list(server)
        for game in games_list:
            games += game + '\n'
        await message.channel.send(f"```Games being played right now: \n{games}```")
    if "!what_game" in message.content.lower():
        game = random.choice(game_list(server))
        await message.channel.send(f"```You should play: {game}```")


client.loop.create_task(game_tracker())
client.loop.create_task(server_metrics())
client.run(token)