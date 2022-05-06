import discord, config
from database import Database
from Commands.CommandHandler import CommandHandler
from listeners.test import Listener


db = Database('./Databases/db.json')
# Bananas = Database('./Databases/Bananas.json')
cmd = CommandHandler('./Commands')
cmd.load_comands()
test = Listener()
client = discord.Client()

@client.event
async def on_ready():
    print(f'[Client] Logged in as {client.user.name}')
    # await client.change_presence(activity=discord.Game(name='!help'))
    #watching x users in x servers activity
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f' {len(client.users)} Monkis in {len(client.guilds)} servers'))
    print(f'[Client] Loaded {len(client.guilds)} guilds')
    print(f'[Client] Loaded {len(client.emojis)} emojis')
    print(f'[Client] Loaded {len(client.users)} users')
    return


# Message Event for the Command Handler
# kai best dev :sob: only took one try real!!1!11
@client.event 
async def on_message(message):
    # User Info.
    userid = str(message.author.id)
    username = str(message.author).split('#')[0]
    usertag = str(message.author).split('#')[1]
    
    # Command Info.
    if message.content.startswith(config.PREFIX):
        pass
    else:
        return
    
    command = message.content.split(' ')[0]
    args = message.content.split(' ')
    args.remove(command)
    command = command.replace(config.PREFIX, '')

    #await test.main(args, message, client, db)
    await cmd.execute_command(command, args, message, client, db)

    if message.content == 'hello':
        await message.channel.send('Hello!')
        
client.run(config.TOKEN)

