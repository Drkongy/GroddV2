import discord
from getset import banana
from lowdb import Low, File


class BananaCommand:
    name = 'farm'
    description = 'farm some bananas'
    usage = 'farm<No Args>'
    aliases = ['f']



    async def main(args, message, client, db):
        FileAdapter = File('./Databases/Economy.json')
        bdb = Low(FileAdapter)
        b = banana(message.author.id)
        #! ==========================================================

        #* set the new balance

        b.addBalance(bdb, message.author.id, b.getBPC())

        embed = discord.Embed(title='Banana Economy - Farm', color=0xFFE338)
        embed.add_field(name=f'You have Made {b.getBPC()} banana(s)!', value=f'You now have {b.getBalance()} bananas(s)! 🍌', inline=True)
        embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
        embed.set_author(name='Economy', icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return



    



        
           

            





        



        
        









