import discord
class Command:
    name = 'cool'
    description = 'does something cool'
    usage = 'cool<No args>'

    async def main(args, message, client, db):
        #make a cool embed 
        embed = discord.Embed(title='Cool', description='Cool', color=0x00ff00)
        embed.set_author(name='Cool', icon_url=message.author.avatar_url)
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return

        