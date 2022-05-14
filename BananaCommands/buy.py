import discord
from getset import banana
from lowdb import Low, File

class BananaCommand():
    name = 'buy'
    description = 'Buy Some monkis'
    usage = 'buy<monki>'
    aliases = ['b']

    #todo MAKE THE ARGS WORK!



    async def main(args, message, client, db):
        FileAdapter = File('./Databases/Economy.json')
        bdb = Low(FileAdapter)
        b = banana(message.author.id)
        #! ==========================================================

        if len(args) == 1:
            #* increase the balance by the bpc
            embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
            embed.add_field(name='How to use: ', value=f'!bananas buy (Monki Name)', inline=False)
            embed.add_field(name='Marmocets (1 BPC) ', value=f'Cost: 10 Banana(s)', inline=True)
            embed.add_field(name='Capuchin (5 BPC) ', value=f'Cost: 100 Banana(s)', inline=True)
            embed.add_field(name='Bonobo (25 BPC) ', value=f'Cost: 1 Thousand Banana(s)', inline=True)
            embed.add_field(name='Orangutan (100 BPC) ', value=f'Cost: 25 Thousand Banana(s)', inline=True)
            embed.add_field(name='Baboon (500 BPC) ', value=f'Cost: 100 Thousand Banana(s)', inline=True)
            embed.add_field(name='Chimpanzee (2000 BPC) ', value=f'Cost: 500 Thousand Banana(s)', inline=True)
            embed.add_field(name='Mandrill (5000 BPC) ', value=f'Cost: 1 Million Banana(s)', inline=True)
            embed.add_field(name='Gelada (10000 BPC) ', value=f'Cost: 5 Million Banana(s)', inline=True)
            embed.add_field(name='Gorilla (25000 BPC) ', value=f'Cost: 25 Million Banana(s)', inline=True)
            embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
            embed.set_author(name='Economy', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return



        elif len(args) >= 2:


            #* =======================================================================
            if args[1].lower() == 'marmocets':
                if b.getBalance() < 10:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 10 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 10)
                b.addBPC(bdb, message.author.id, 1)
                b.addMarmocets(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought a Marmocet!', value=f'You now have {b.getMarmocets()} Marmocets(s) 🐒', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 10} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/marmocets.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

            #* =======================================================================

            elif args[1].lower() == 'capuchin':
                if b.getBalance() < 100:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 100 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/capuchin.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 100)
                b.addBPC(bdb, message.author.id, 5)
                b.addCapuchin(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought a Capuchin!', value=f'You now have {b.getCapuchin()} Capuchin(s) 🐵', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 100} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/capuchin.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

            #* =======================================================================


            elif args[1].lower() == 'bonobo':
                if b.getBalance() < 1000:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 1,000 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/bonobo.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 1000)
                b.addBPC(bdb, message.author.id, 25)
                b.addBonobo(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought a Bonobo!', value=f'You now have {b.getBonobo()} Bonobo(s) 🦍', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 1000} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/bonobo.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return


            #* =======================================================================

            elif args[1].lower() == 'orangutan':
                if b.getBalance() < 10000:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 25,000 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/orangutan.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 25000)
                b.addBPC(bdb, message.author.id, 100)
                b.addOrangutan(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought an Orangutan!', value=f'You now have {b.getOrangutan()} Orangutan(s) 🦍', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 10000} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/orangutan.png')
                await message.channel.send(embed=embed)
                return
            #* =======================================================================

            elif args[1].lower() == 'baboon':
                if b.getBalance() < 100000:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 100,000 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/baboon.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 100000)
                b.addBPC(bdb, message.author.id, 500)
                b.addBaboon(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought a Baboon!', value=f'You now have {b.getBaboon()} Baboon(s) 🦛', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 100000} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/baboon.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

            #* =======================================================================

            elif args[1].lower() == 'chimpanzee':
                if b.getBalance() < 500000:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 500,000 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/chimpanzee.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 500000)
                b.addBPC(bdb, message.author.id, 2000)
                b.addChimpanzee(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought a Chimpanzee!', value=f'You now have {b.getChimpanzee()} Chimpanzee(s) 🦘', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 500000} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/Chimpanzee.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

            #* =======================================================================

            elif args[1].lower() == 'mandrill':
                if b.getBalance() < 1000000:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 1,000,000 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/mandrill.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 1000000)
                b.addBPC(bdb, message.author.id, 5000)
                b.addMandrill(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought a Mandrill!', value=f'You now have {b.getMandrill()} Mandrill(s) 🦜', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 1000000} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/mandrill.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

            #* =======================================================================

            elif args[1].lower() == 'gelada':
                if b.getBalance() < 5000000:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 5,000,000 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/gelada.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 5000000)
                b.addBPC(bdb, message.author.id, 10000)
                b.addGelada(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought a Gelada!', value=f'You now have {b.getGelada()} Gelada(s) 🦟', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 5000000} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Gelada.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

            #* =======================================================================

            elif args[1].lower() == 'gorilla':
                if b.getBalance() < 25000000:
                    embed = discord.Embed(title='insufficent Funds', color=0xFF0000)
                    embed.add_field(name='Not enough bananas!', value=f'You need at least 25,000,000 bananas to buy this!', inline=False)
                    embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                    embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/Images/gorilla.png')
                    embed.set_footer(text='Made by Zeeshan & Kai')
                    await message.channel.send(embed=embed)
                    return
                b.setBalance(bdb, message.author.id, b.getBalance() - 25000000)
                b.addBPC(bdb, message.author.id, 25000)
                b.addGorilla(bdb, message.author.id, 1)
                #make an embed 
                embed = discord.Embed(title='Banana Economy - Monkis', color=0xFFE338)
                embed.add_field(name='You bought a Gorilla!', value=f'You now have {b.getGorilla()} Gorilla(s) 🦍', inline=False)
                embed.add_field(name=f'You now make {b.getBPC()} ', value=f'Your balance is {b.getBalance() - 25000000} Bananas(s) 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/BananaClickerMobile/BananaClickerMobileAssets/gorilla.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

            #* =======================================================================




            



            

            else:
                embed = discord.Embed(title='Invalid Monki', color=0xFF0000)
                embed.add_field(name='Invalid Monki', value=f'That monki does not exist', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return


            
            
                    






        return



        #get banana varible from bananas.py




    



        
           

            





        



        
        









