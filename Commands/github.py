import discord
class Command:
    name = 'github'
    description = 'Sends you to the github repository'
    usage = 'github<No args>'

    async def main(args, message, client, db):
        embed = discord.Embed(title='Github', description='Click the link to go to the github repository' ,url='https://github.com/', color=0x00ff00)
        embed.set_author(name='Github', icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon3.png')
        embed.set_image(url = "https://github-link-card.s3.ap-northeast-1.amazonaws.com/Drkongy/BananaClickerMobile.png")
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return