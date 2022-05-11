import discord
class BananaCommand:
    name = 'test'
    description = 'test'
    usage = 'test<No args>'

    async def main(args, message, client, db):
        embed = discord.Embed(title='test', description='test', color=0x00ff00)
        embed.set_author(name='test', icon_url=message.author.avatar_url)
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return

        