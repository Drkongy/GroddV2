import discord
class Command:
    name = 'info'
    description = 'Shows infomation about the bot'
    usage = 'info<No Args>'

    async def main(args, message, client, db):
        embed = discord.Embed(title='Infomation', url="https://www.kongolian.tech/", color=0x000000)
        embed.set_author(name='Zeeshan', icon_url=message.author.avatar_url)
        embed.add_field(name='Hello!', value= "I'm Zeeshan!\n I'm a Computer Science Student. \nMy main project is a game called BananaClicker!\nThis discord bot is a small economy game which is based on the Banana Clicker game.\n Thanks for checking it out, it means a lot! ", inline=False)
        # embed.add_field(name='My website', value= "http://www.kongolain.tech/", url='http://www.kongolain.tech/', inline=False)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon3.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return

        