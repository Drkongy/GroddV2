import os, importlib, discord

class BananaCommand:
    name = 'help'
    description = 'Displays all of the help commands for Banana Economy'
    usage = 'help<No Args>'


    
    async def main(args, message, client, db):
        if len(args) == 1:
            embed = discord.Embed(title='Banana Commands: ', color=0x00ff00)
            embed.set_author(name='Help', icon_url=message.author.avatar_url)
            for BananaCommand in os.listdir('./BananaCommands'):
                if BananaCommand.endswith('.py') and BananaCommand != 'BananaHandler.py' and BananaCommand != 'help.py':
                    BananaCommand = BananaCommand.split('.')[0]
                    embed.add_field(name=BananaCommand, value=importlib.import_module(f"BananaCommands.{BananaCommand}").BananaCommand.description, inline=True)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return
        else:
            embed = discord.Embed(title='Invalid Arguments ❌', description='Please use correct arguments from !help', color=0xff0000)
            embed.set_author(name='Help', icon_url=message.author.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
        return
    



        
           

            





        



        
        









