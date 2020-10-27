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

async def nmb_of_mamacos():
    chan_to_send = None
    for chan in client.guilds[0].text_channels:
        if chan.name == 'plebe':
            chan_to_send = chan
            break
    actual_voice_channel = None

    while True:
        msg = ""


        nmb_of_chan = client.guilds[0].voice_channels
        nmb_of_chan.sort(reverse=True, key=lambda chan: len(chan.members))

        for chan in client.guilds[0].voice_channels:
            msg += chan.name + " tem " + str(len(chan.members)) + " mamacos.\n"

        print(msg)
        
        # apenas craig na sala
        if actual_voice_channel is not None and len(actual_voice_channel.members) == 1:
            await chan_to_send.send(':craig: sair ' + actual_voice_channel.name)

        print(nmb_of_chan[0].members)
        if len(nmb_of_chan[0].members) > 0: 
            if actual_voice_channel is not None: continue
            await chan_to_send.send(':craig: entrar ' + nmb_of_chan[0].name)
            actual_voice_channel = nmb_of_chan[0]

        await asyncio.sleep(1800)

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
