import discord
from discord.ext import tasks
import asyncio
import random
from modules.meme_songs import MemeSongs
from modules.logger import Logger
from modules.audio_splitter import AudioSplitter
import logging

client = discord.Client()
meme_songs = None


@client.event
async def on_message(message):
    """
    Method that triggers when bot receives any message. 
    
    Keyword arguments:
        message -- Message that triggers the event.

    Return:
        None
    """
    if message.author == client.user and message.content.startswith(':craig:'):
        await message.delete()
        return
    if 'Craig#1289' == '{0.author}'.format(message):
        logging.info(message.content.split(' ')[-1][:-1])
        await message.delete()
        return
    if message.content.startswith('$dnama'):
        await message.channel.send(':craig:' + message.content[6:])


async def nmb_of_mamacos():
    """
    Bot calculate the number of members on plebe channel and
    send random meme songs when the channel have at least one member. 
    
    Keyword arguments:
        None

    Return:
        None
    """
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

        logging.info(msg)

        if len(nmb_of_chan[0].members) > 0:

            logging.info(nmb_of_chan[0].name)
            vc = await nmb_of_chan[0].connect()
            choosen_audio = meme_songs.songs[random.randint(
                0, len(meme_songs.songs) - 1)]
            logging.info(choosen_audio)
            audio_s = discord.FFmpegPCMAudio(choosen_audio)
            vc.play(audio_s)

            while vc.is_playing():
                await asyncio.sleep(1)
            # disconnect after the player has finished
            vc.stop()
            await vc.disconnect()

        await asyncio.sleep(1800)


@client.event
async def on_ready():
    """
    Method called when discord bot finished the setup methods.
    
    Keyword arguments:
        None

    Return:
        None
    """
    logging.info('Pai ta on como {0.user}'.format(client))
    await nmb_of_mamacos()


def main():
    Logger()
    logging.info('Starting bot...')

    global meme_songs

    meme_songs = MemeSongs()
    
    with open('token.key') as token:
        client.run(token.read())

if __name__ == '__main__':
    main()
