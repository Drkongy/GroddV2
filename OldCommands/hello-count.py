class Command:
    name = 'Hello Count'
    description = 'Returns the times you\'ve said hello!'
    usage = 'hello-count <No Args>'
    
    async def main(args, message, client, db):
        hello_count = db.get(f'{message.author.id}-hello-count')
        if hello_count != None:
            await message.channel.send(f'You have said Hello {hello_count} times!')
        else:
            await message.channel.send(f'You haven\'t said Hello yet :(')
        return

        
