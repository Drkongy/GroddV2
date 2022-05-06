import discord
class Command:
    name = 'invite'
    description = 'Allows you to invite the bot to your server'
    usage = 'invite<No Args>'


    async def main(args, message, client, db):
        embed = discord.Embed(color=0x000000)
        embed.set_author(name='Zeeshan', icon_url=message.author.avatar_url)
        embed.add_field(name='Invite Link:', value='[Click Here](https://discordapp.com/api/oauth2/authorize?client_id=715010989843791872&permissions=8&scope=bot)', inline=False)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/icon10.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return


        