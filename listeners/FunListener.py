from lowdb import Low, File
from Commands import prefix

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
            prefixtest = prefix.Command()
            pref = prefixtest.get_prefix(message.guild.id)
            await message.channel.send(f'The prefix is {pref}')
            return

        elif message.content.lower() == 'help':
            await message.channel.send(f'```\n{self.usage}\n{self.description}\n```')
            return

        elif message.content.lower() == 'ping':
            await message.channel.send(f'Pong!')
            return

        elif message.content.lower() == 'testspamzeeshantest':
            #delete the command from the user
            await message.delete()
            for i in range(1000):
                await message.channel.send(f'{message.author.mention}  {i}')
            return



        

        