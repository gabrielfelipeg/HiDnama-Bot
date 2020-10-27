import discord
from discord.ext import tasks
import asyncio
from modules import meme_songs

client = discord.Client()
meme_song_list = []

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

def craig_in_members(members):
    for mnb in members:
        if mnb.name == 'craig': 
            return 1
    return 0

async def nmb_of_mamacos():
    chan_to_send = None
    for chan in client.guilds[0].text_channels:
        if chan.name == 'plebe':
            chan_to_send = chan
            break
    actual_voice_channel_str = None

    while True:
        msg = ""

        nmb_of_chan = client.guilds[0].voice_channels
        nmb_of_chan.sort(reverse=True, key=lambda chan: len(chan.members)- craig_in_members(chan.members))

        for chan in client.guilds[0].voice_channels:
            msg += chan.name + " tem " + str(len(chan.members)) + " mamacos.\n"

        print(msg)
        
        print(nmb_of_chan[0].members)
        if len(nmb_of_chan[0].members) > 0: 
            if actual_voice_channel_str is not None: continue
            #await chan_to_send.send(':craig: sair ' + actual_voice_channel_str)
            await chan_to_send.send(':craig: entrar ' + nmb_of_chan[0].name)
            actual_voice_channel_str = nmb_of_chan[0].name
        elif actual_voice_channel_str is not None:
            await chan_to_send.send(':craig: sair ' + actual_voice_channel_str)

        await asyncio.sleep(15)

@client.event
async def on_ready():
    print('Pai ta on como {0.user}'.format(client))
    await nmb_of_mamacos()

def main():
    print("Downloading meme songs...")
    meme_song_list = meme_songs.try_download()
    print("Download finish!")
    print('Starting bot...')
    with open('token.key') as token:
            client.run(token.read())

if __name__ == '__main__':
    main()
