import discord
from lowdb import Low, File
from getset import banana



class BananaCommand:
    name = 'balance'
    description = 'gets the players balance'
    usage = 'balance<No Args>'
    aliases = ['bal']




    
    async def main(args, message, client, db):
        #init the database
        b = banana(message.author.id) # this inits the getter and setter

        #! ==========================================================
        #* If the bananas command is done.
        embed = discord.Embed(title='Banana Economy', color=0xFFE338)
        embed.add_field(name='Bananas Balance: ', value=f'You have {b.getBalance()} bananas! 🍌', inline=False)
        embed.add_field(name='Bananas per command: ', value=f'You Make {b.getBPC()} banana(s) per command! 🤑', inline=True)
        embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
        embed.set_author(name='Economy', icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return


    



        
           

            





        



        
        









