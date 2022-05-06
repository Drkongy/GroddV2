import discord
class Command:
    name = 'say'
    description = 'Says what the user says then deltes the users message'
    usage = 'say <Text>'


    async def main(args, message, client, db):
        if len(args) > 0:
            await message.delete()
            with open('Databases/sayLog.txt', 'a') as f:
                #write the time the message was sent
                f.write(f'[{message.created_at.strftime("%d/%m/%Y %H:%M:%S")}] ')
                f.write(f'{message.guild.name} - {message.author} ::  {" ".join(args)}\n')
            await message.channel.send(' '.join(args))
        else:
            embed = discord.Embed(title='Invalid Arguments ❌', description='Please use make sure you are saying something!', color=0xff0000)
            embed.set_author(name='Zeeshan', icon_url=message.author.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return          

        