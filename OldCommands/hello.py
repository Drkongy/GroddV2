class Command:
    name = 'Hello'
    description = 'says hello'
    usage = 'hello<No Args>'


    
    async def main(args, message, client, db):
        hello_count = db.get(f'{message.author.id}-hello-count')
        if hello_count == None:
            db.set(f'{message.author.id}-hello-count', 1)
            hello_count = 1
        else:
            db.set(f'{message.author.id}-hello-count', hello_count + 1)
            hello_count += 1
        await message.channel.send(f'Hello {message.author.name}!')
        return

        