import discord
from discord.ext import tasks
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user and message.content.startswith(':craig:'):
        await message.delete()
        return
    if 'Craig#1289' == '{0.author}'.format(message):
        print(message.content.split(' ')[-1][:-1])
        await message.delete()
        return
    if message.content.startswith('$dnama'):
        await message.channel.send(':craig:' + message.content[6:])

async def nmb_of_mamacos():
    while True:
        chan_to_send = None
        for text_chan in client.guilds[0].text_channels:
            if text_chan.name == 'plebe':
                chan_to_send = text_chan
                break
        msg = ""
        for chan in client.guilds[0].voice_channels:
            msg += chan.name + " tem " + str(len(chan.members)) + " mamacos.\n"
        await chan_to_send.send(msg)
        await asyncio.sleep(60)

@client.event
async def on_ready():
    await nmb_of_mamacos()

with open('token.key') as token:
    client.run(token.read())
