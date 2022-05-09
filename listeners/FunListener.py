from lowdb import Low, File
class FunListener:
    def __init__(self):
        self.name = 'FunListener'
        self.description = 'Listens for fun commands'
        self.usage = 'Just write anything and it will pick something up'
        FileAdapter = File('./Databases/db.json')
        db = Low(FileAdapter) 

        self.db = db

    def load(self):
            print(f'[ListenerHandler] Loaded {self.name}')
    

    #* these are random fun listener commands.
    
    async def main(self, args, message, client):


        user = message.author.name
        if message.content.lower() == 'hello':
            await message.channel.send('Hello!')
        elif message.content.lower() == 'bye':
            await message.channel.send(f'Goodbye Mother Fucker')
            return
        elif message.content.lower() == 'rehan':
            await message.channel.send(f'kusrah terah mava lugana')
            return
        elif message.content.lower() == 'kusrah':
            await message.channel.send(f'https://www.youtube.com/watch?v=3yvY2LRgdbg&ab_channel=RAJA')
            return
        elif message.content.lower() == 'kusrah2':
            await message.channel.send(f'#play https://www.youtube.com/watch?v=3yvY2LRgdbg&ab_channel=RAJA')
            return
        elif message.content.lower() == 'banana':
            await message.channel.sent(f':banana:')
            return
        elif message.content.lower() == 'grodd suck my dick':
            await message.channel.send(f'Your Cock Is Too Small {user}')
            return

        elif message.content.lower() == 'prefix':
            #get prefix from test database
            prefix = self.db.get(f'Guilds.${message.guild.id}.Prefix')
            #send prefix to channel
            await message.channel.send(f'The prefix is {prefix}')
            return


        

        