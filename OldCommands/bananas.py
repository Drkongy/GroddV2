import discord

class Command:
    name = 'Bananas'
    description = 'Kongolian Banana Economy!'
    usage = 'Bananas<no args>'


    
    async def main(args, message, client, db):
        try:
            bananas = db.user(message.author.id, ['Balance'])
            BPC = db.user(message.author.id, ['BPC'])
        except:
            db.user(message.author.id, {'Balance': 0}, 0)
            db.set(message.author.id, {'BPC': 1}, 1)
            user = db.get(message.author.id)
            bananas = user['Balance']
            BPC = user['BPC']



        #* If the bananas command is done.
        if len(args) == 0:
            # if bananas == None:
            #     db.user(message.author.id, 'Balance', 1)
            #     db.user(message.author.id, 'BPC', 1)
            #     # db.user(f'{message.author.id}', 'Balance', 1)
            #     # db.user(f'{message.author.id}', 'BPC', 1)
            #     bananas = 1
            #     BPC = 1
            # #else:
            #     #db.set(f'{message.author.id}-Balance', bananas + BPC)
            #     #bananas += BPC
            embed = discord.Embed(title='Banana Economy', color=0xFFE338)
            embed.add_field(name='Bananas Balance: ', value=f'You have {bananas} bananas! 🍌', inline=False)
            embed.add_field(name='Bananas per command: ', value=f'You Make {BPC} banana(s) per command! 🤑', inline=True)
            embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
            embed.set_author(name='Economy', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
            embed.set_footer(text='Made by Zeeshan & Kai')
            


            await message.channel.send(embed=embed)
            return
        









        #*Arguments
        if len(args) == 1:
            #* If the user wants to see how much balance they have.
            if args[0] == 'Balance' or args[0] == 'bal' or args[0] == 'balance':
                embed = discord.Embed(title='Banana Economy - Balance', color=0xFFE338)
                embed.add_field(name='Bananas Balance: ', value=f'You have {bananas} bananas! 🍌', inline=False)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return



            #* If the user wants to see how much bananas they make per command.
            elif args[0] == 'farm' or args[0] == 'Farm' or args[0] == 'FARM':
                db.set(f'{message.author.id}-Balance', bananas + BPC)
                bananas += BPC
                embed = discord.Embed(title='Banana Economy - Farm', color=0xFFE338)
                embed.add_field(name=f'You have Made {BPC} banana(s)!', value=f'You now have {bananas} bananas(s)! 🍌', inline=True)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return




            elif args[0] == 'upgrade' or args[0] == 'Upgrade' or args[0] == 'upgr':
                embed = discord.Embed(title='Banana Economy - Upgrades', color=0xFFE338)
                embed.add_field(name='How to use: ', value=f'!bananas upgrade (upgrade_name) (OPTIONAL AMOUNT)', inline=False)
                embed.add_field(name='Marmocets (1 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Capuchin (5 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Bonobo (25 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Orangutan (100 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Baboon (500 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Chimpanzee (2000 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Mandrill (5000 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Gelada (10000 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Gorilla (25000 BPC) ', value=f'Cost: 20 Banana(s)', inline=True)
                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

















            #!remember to keep on updating the help commands
            #* if the user wants to see the help commands for bananas 
            elif args[0] == 'help' or args[0] == 'Help' or args[0] == 'HELP':
                embed = discord.Embed(title='Banana Economy - Help', color=0xFFE338)
                #! ===========================================================================
                embed.add_field(name='!bananas : ', value=f'Show the main panel', inline=False)
                embed.add_field(name='!bananas help: ', value=f'Shows this panel', inline=False)
                embed.add_field(name='!bananas balance: ', value=f'Shows the Balance', inline=False)
                embed.add_field(name='!bananas farm: ', value=f'Farms for some bananas', inline=False)
                embed.add_field(name='!bananas upgrade: ', value=f'Shows the Upgrades', inline=False)



                #! ===========================================================================

                embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
                embed.set_author(name='Economy', icon_url=message.author.avatar_url)
                embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon2.png')
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)





            #! if the arugments are incorrect it would show this stuff
            else:
                embed = discord.Embed(title='Invalid Arguments ❌', description='Please use correct arguments from !Bananas help', color=0xff0000)
                embed.set_author(name='Banana Economy', icon_url=message.author.avatar_url)
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return
        else:
            embed = discord.Embed(title='Invalid Arguments ❌', description='Please use correct arguments from !Bananas help', color=0xff0000)
            embed.set_author(name='Banana Economy', icon_url=message.author.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)

            



        