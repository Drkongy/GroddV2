class Listener:
    def __init__(self):
        self.name = 'test'
        self.description = 'Test'
        self.usage = 'test'
    


    
    async def main(args, message, client, db):
        #if the message is = hello then do command stuff
        if message.content == 'hello':
            await message.channel.send('Hello!')

        # hello_count = db.get(f'{message.author.id}-hello-count')
        # if hello_count == None:
        #     db.set(f'{message.author.id}-hello-count', 1)
        #     hello_count = 1
        # else:
        #     db.set(f'{message.author.id}-hello-count', hello_count + 1)
        #     hello_count += 1
        # await message.channel.send(f'Hello {message.author.name}!')
        # return
        

        