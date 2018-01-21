import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'): # si tu veux fairre d'autre commande tu copie ca par exemple
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!wyrd'):
        await client.delete_message(message)
        await client.send_message(message.channel,"Wyrd t bo :heart:",)

    elif message.content.startswith('!del'):
        await client.delete_message(messages) 	                                                                                                                                
        
    elif message.content.startswith('!hitsu'):
        await client.delete_message(message)
        await client.send_message(message.channel,"Coucou ! o/",)

    elif message.content.startswith('!make tequila'):
        await client.delete_message(message)
        await client.send_message(message.channel,"Tenez, voici votre tequila, ça fera 5 € :wink:")

    elif message.content.startswith('!nani'):
        await client.delete_message(message)
        await client.send_message(message.channel,"Omae wa mou shindeiru")
        await client.send_message(message.channel,"NANI ?!")

    elif "sardoche" in message.content :
        await client.send_message(message.channel,"Sardoche, le mec qui fait des streams en caleçons et qui gueule sur ses viewers h24 ?")

    elif "seiya" in message.content :
        await client.send_message(message.channel, "Les chevaliers du zodiaaaaaque, ils sont toujours à l'attaaaaaque")
        
client.run('NDAyNDgyNDA0Mzk0MjcwNzIx.DT6ODg.yafBAEk0rJM43l85Xm_Pxi5I__4') #tu cole direct ta token
