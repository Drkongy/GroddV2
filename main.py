import discord, config
from Commands.CommandHandler import CommandHandler
from BananaCommands.BananaHandler import BananaHandler
from listeners.FunListener import FunListener
from listeners.logger import Listener
from lowdb import Low, File
from Commands import prefix




#declare the prefix class 
prefixtest = prefix.Command()

# initilizes the Handlers
logger = Listener()
fun = FunListener()
cmd = CommandHandler('./Commands')
banana = BananaHandler('./BananaCommands')


#Prints the loaded data.
cmd.load_comands()
banana.print()
logger.load()
fun.load()




# logger = Listener()
client = discord.Client()
FileAdapter = File('./Databases/db.json')
db = Low(FileAdapter)




# on when bot joins a server 

@client.event
async def on_gui_joined(guild):
    db.set(f'Guilds.${guild.id}.Prefix', '!') # Returns self, so that you can use .write() to write to json
    db.write() # Writes memory to json
    print(f'Joined {guild.name}')
    print(f'{guild.id}')



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'!help | {len(client.guilds)} Servers'))
    print(f'[Client] Logged in as {client.user.name}')
    print(f'[Client] Loaded {len(client.guilds)} guilds')
    print(f'[Client] Loaded {len(client.emojis)} emojis')
    print(f'[Client] Loaded {len(client.users)} users')


    ##* get id of all the guilds and gives it the default prefix.
    # for guild in client.guilds:
    #     #get id of all Users
    #     db.set(f'Guilds.${guild.id}.Prefix', '!') # Returns self, so that you can use .write() to write to json
    #     db.write() # Writes memory to json
    
    

# Message Event for the Command Handler & ListenerHandler
@client.event 
async def on_message(message):
    prefix = prefixtest.get_prefix(message.guild.id)
    # Command Info.
    args = message.content.split(' ')
    await logger.main(args, message, client)
    await fun.main(args, message, client)

    if message.content.startswith(prefix):
        pass
    else:
        return
    command = message.content.split(' ')[0]
    args.remove(command)
    command = command.replace(prefix, '')
    await cmd.execute_command(command, args, message, client, db)
    return


client.run(config.TOKEN) 