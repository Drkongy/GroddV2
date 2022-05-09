import discord
import random

TOKEN = 'NOT IN USE'#
PREFIX = '!'
banana = 0;

client = discord.Client()

@client.event
async def on_ready():
    print(f'[Bot] I have logged in as {client.user}')
    bananas = 0
    

@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_id = str(message.author.id)
    Discord_tag = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{Discord_tag}: ({channel}) :: {user_message}')
    
    #if message.author == client.user:
    #    return


    #make a prefix system
    if user_message.startswith(PREFIX + 'banana'):
        bananas += 1
        await message.channel.send(f'{username} has {bananas} banana(s)')
        print(f'{username} has {bananas} banana(s)')
    elif user_message.startswith(PREFIX + 'reset'):
        bananas = 0
        await message.channel.send(f'{username} has {bananas} banana(s)')
        print(f'{username} has {bananas} banana(s)')
    elif user_message.startswith(PREFIX + 'help'):
        await message.channel.send('!banana - gives you a banana \n!reset - resets the banana counter \n!help - shows this message')
    elif user_message.startswith(PREFIX + 'ping'):
        await message.channel.send('Pong!')
    # DB Test Code
    elif user_message.startswith(PREFIX + 'hello-count'):
        hello_count = db.get(f'{user_id}-hello-count')
        if hello_count != None:
            await message.channel.send(f'You have said Hello {hello_count} times!')
        else:
            await message.channel.send(f'You haven\'t said Hello yet :(')
    # DB Test Code End.




    # #if message.channel.name == 'test':   ## if you want to bot to look in a specific channel for these commands.
    if user_message.lower() == 'hello':
        # DB Test Code
        hello_count = db.get(f'{user_id}-hello-count')
        if hello_count == None:
            db.set(f'{user_id}-hello-count', 1)
        else:
            db.set(f'{user_id}-hello-count', hello_count + 1)
        await message.channel.send(f'Hello {username}')
        return
    # elif user_message.lower() == 'bye':
    #     await message.channel.send(f'Goodbye Mother Fucker')
    #     return
    # elif user_message.lower() == 'rehan':
    #     await message.channel.send(f'kusrah terah mava lugana')
    #     return
    # elif user_message.lower() == 'kusrah':
    #     await message.channel.send(f'https://www.youtube.com/watch?v=3yvY2LRgdbg&ab_channel=RAJA')
    #     return
    # elif user_message.lower() == 'kusrah2':
    #     await message.channel.send(f'#play https://www.youtube.com/watch?v=3yvY2LRgdbg&ab_channel=RAJA')
    #     return
    # elif (user_message.lower == 'banana'): #or user_message.lower == '!b'):
    #     #bananas =+ 1
    #     await message.channel.sent(f'Bananas: ')# + bananas)
    #     return
    # elif user_message.lower() == 'bot suck my dick':
    #     await message.channel.send(f'Your Cock Is Too Small {username}')
    #     return


client.run(TOKEN)