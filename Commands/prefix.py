import discord, config
class Command:
    name = 'prefix'
    description = 'Allows you to change the prefix'
    usage = 'prefix<Prefix>'

    async def main(args, message, client, db):
        if len(args) > 0:
            config.PREFIX = "".join(args[0])
            embed = discord.Embed(title='Prefix changed! ✅', description='The new prefix is: ' + config.PREFIX, color=0x00ff00)
            embed.set_author(name='Prefix', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon3.png')
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return
        else:
            embed = discord.Embed(title='Prefix', description='The current prefix is: ' + config.PREFIX, color=0x00ff00)
            embed.set_author(name='Prefix', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon3.png')
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return

            


        