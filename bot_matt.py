import discord
import asyncio
from discord.ext.commands import Bot

client = discord.Client()
description = 'Jérémy'

client = Bot(command_prefix=";;", description=description, self_bot=True)

@client.event
async def on_ready():
    print('Log in :')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):


    if message.content.startswith('!msg'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Les messages sont en train d être calculés...')
        async for log in client.logs_from(message.channel, limit=200):
            if log.author == message.author:
                counter += 1
        await client.send_message(message.channel, "<@" + message.author.id + "> Vous avez {} messages.".format(counter))



client.run("Mjc1NzEwMjQ5MzUwOTg3Nzg4.DTo-aQ.8jg66gJziAz5Hqeimfc-q9D0CeA", bot=False)
