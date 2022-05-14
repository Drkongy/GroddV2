import discord
from BananaCommands.BananaHandler import BananaHandler
from lowdb import Low, File
from getset import banana




class Command:
    name = 'bananas'
    description = 'Kongolian Banana Economy!'
    usage = 'bananas<no args>'
    aliases = ['b', 'banana', 'bananas']

    # global cmd



    async def __init__(self):
        cmd = BananaHandler('./BananaCommands')
        cmd.load_comands()
        self.cmd = cmd
        print('Loaded Bananas')

    
    async def main(args, message, client, db):
        #init the database
        FileAdapter = File('./Databases/db.json')
        db = Low(FileAdapter)
        b = banana(message.author.id) # this inits the getter and setter

        #! ==========================================================
        #* If the bananas command is done.
        if len(args) == 0:
            embed = discord.Embed(title='Banana Economy', color=0xFFE338)
            embed.add_field(name='Bananas Balance: ', value=f'You have {b.getBalance()} bananas! 🍌', inline=False)
            embed.add_field(name='Bananas per command: ', value=f'You Make {b.getBPC()} banana(s) per command! 🤑', inline=True)
            embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
            embed.set_author(name='Economy', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return
        
        #* If the user wants to buy bananas
        elif len(args) >= 1:
            cmd = BananaHandler('./BananaCommands')
            cmd.load_comands()
            await cmd.execute_command(args[0], args, message, client, db)
            return






    



        