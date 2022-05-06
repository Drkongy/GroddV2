import os, importlib, discord

class Command:
    name = 'help'
    description = 'Displays all of the help commands'
    usage = 'help<No Args>'


    
    async def main(args, message, client, db):
        if len(args) == 0:
            embed = discord.Embed(title='Commands: ', color=0x00ff00)
            embed.set_author(name='Help', icon_url=message.author.avatar_url)
            for command in os.listdir('./Commands'):
                if command.endswith('.py') and command != 'CommandHandler.py':
                    command = command.split('.')[0]
                    embed.add_field(name=command, value=importlib.import_module(f"Commands.{command}").Command.description, inline=False)
            embed.set_footer(text='Made by Zeeshan & Kai')

            await message.channel.send(embed=embed)
            return
        elif len(args) == 1:
            if args[0] == 'test':
                await message.channel.send('Test')
                return
            else:
                embed = discord.Embed(title='Invalid Arguments ❌', description='Please use correct arguments from !help', color=0xff0000)
                embed.set_author(name='Help', icon_url=message.author.avatar_url)
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return
        else:
            embed = discord.Embed(title='Invalid Arguments ❌', description='Please use correct arguments from !help', color=0xff0000)
            embed.set_author(name='Help', icon_url=message.author.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
        return
    



        
           

            





        



        
        









