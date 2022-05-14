import discord
from getset import banana
from lowdb import Low, File


class BananaCommand:
    name = 'inventory'
    description = 'Shows All Your Monkis'
    usage = 'Inventory<No Args>'
    aliases = ['inv']





    async def main(args, message, client, db):
        # FileAdapter = File('./Databases/Economy.json')
        # bdb = Low(FileAdapter)
        b = banana(message.author.id)
        #! ==========================================================


        # make an embed that shows all the monkis owned 
        embed = discord.Embed(title='Monki Inventory', color=0xFFE338)
        embed.add_field(name='Marmocets Owned: ', value=f'You have {b.getMarmocets()} Marmocet(s)!', inline= True)
        embed.add_field(name='Capuchin Owned: ', value=f'You have {b.getCapuchin()} Capuchin(s)!', inline=True)
        embed.add_field(name='Bonobo Owned: ', value=f'You have {b.getBonobo()} Bonobo(s)!', inline=True)
        embed.add_field(name='Orangutan Owned: ', value=f'You have {b.getOrangutan()} Orangutan(s)!', inline=True)
        embed.add_field(name='Baboon Owned: ', value=f'You have {b.getBaboon()} Baboon(s)!', inline=True)
        embed.add_field(name='Chimpanzee Owned: ', value=f'You have {b.getChimpanzee()} Chimpanzee(s)!' , inline=True)
        embed.add_field(name='Mandrill Owned: ', value=f'You have {b.getMandrill()} Mandrill(s)!', inline=True)
        embed.add_field(name='Gelada Owned: ', value=f'You have {b.getGelada()} Gelada(s)!', inline=True)
        embed.add_field(name='Gorilla Owned: ', value=f'You have {b.getGorilla()} Gorilla(s)!', inline=True)
        embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
        embed.set_author(name='Economy', icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return



    



        
           

            





        



        
        









