import discord
from lowdb import Low, File




client = discord.Client()
FileAdapter = File('./Databases/test.json')
db = Low(FileAdapter)



@client.event
async def on_ready():

    print(f'[Client] test')

    






# Message Event for the Command Handler & ListenerHandler
@client.event 
async def on_message(message):
    #check if the message is hello
    if message.content.startswith('hello'):
        #get the user that sent the message

        db.set(f'Guilds.${message.guild.id}.Users.{message.author.id}.Economy.balance', 69420) # Returns self, so that you can use .write() to write to json
        db.write() # Writes memory to json
        await message.channel.send('Hello!')
        return
    #check if the message is ping
    if message.content.startswith('ping'):
        #get the data from the database
        data = db.get(f'Guilds.${message.guild.id}.Users.{message.author.id}.Economy.balance')
        #send the data to the channel
        await message.channel.send(f'{data}')
        return
    if message.content.startswith('set'):
        db.set(f'Guilds.${message.guild.id}.Users.{message.author.id}.Economy.balance', 1)
        db.write()
        await message.channel.send('data set to 1 test')


        




   

client.run(config.TOKEN)

