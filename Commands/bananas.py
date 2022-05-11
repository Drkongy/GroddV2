import discord
from BananaCommands.BananaHandler import BananaHandler
from lowdb import Low, File



class Command:
    name = 'Bananas'
    description = 'Kongolian Banana Economy!'
    usage = 'Bananas<no args>'

    # global cmd



    async def __init__(self):
        cmd = BananaHandler('./BananaCommands')
        cmd.load_comands()
        self.cmd = cmd
        print('Loaded Bananas')

    
    async def main(args, message, client, db):
        FileAdapter = File('./Databases/Economy.json')
        db = Low(FileAdapter)


        # if the usee id is not found in the database
        if db.get(f'Economy.${message.author.id}.Balance') is None:
            db.set(f'Economy.${message.author.id}.Balance', '0') 
            db.set(f'Economy.${message.author.id}.BPC', '1')
            db.write()
            bananas = db.get(f'Economy.${message.author.id}.Balance')
            BPC = db.get(f'Economy.${message.author.id}.BPC')

        else:
            bananas = db.get(f'Economy.${message.author.id}.Balance')
            BPC = db.get(f'Economy.${message.author.id}.BPC')

        #* If the bananas command is done.
        if len(args) == 0:
            embed = discord.Embed(title='Banana Economy', color=0xFFE338)
            embed.add_field(name='Bananas Balance: ', value=f'You have {bananas} bananas! 🍌', inline=False)
            embed.add_field(name='Bananas per command: ', value=f'You Make {BPC} banana(s) per command! 🤑', inline=True)
            embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
            embed.set_author(name='Economy', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return
        
        #* If the user wants to buy bananas
        elif len(args) == 1:
            # print(args[0])
            cmd = BananaHandler('./BananaCommands')
            cmd.load_comands()
            await cmd.execute_command(args[0], args, message, client, db)
            return



    



        