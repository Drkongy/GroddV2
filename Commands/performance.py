import discord, psutil, datetime
class Command:
    name = 'performance'
    description = 'Checks the performance of the bot'
    usage = 'performance<No args>'

    async def main(args, message, client, db):
        embed = discord.Embed(title='Performance', color=0xFFE338)
        embed.add_field(name='Current Time: ', value=f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}', inline=False)
        embed.add_field(name='CPU Usage: ', value=f'{psutil.cpu_percent()}%', inline=False)
        embed.add_field(name='RAM Usage: ', value=f'{psutil.virtual_memory().percent}%', inline=False)
        embed.add_field(name='Connection Speed: ', value=f'{round(client.latency * 1000)}ms', inline=False)
        embed.add_field(name='Boot Time: ', value=f'{datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d/%m/%Y %H:%M:%S")}', inline=False)
        embed.add_field(name='Uptime: ', value=f'{datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())}', inline=False)
        embed.add_field(name='Issued by: ', value=f'{message.author.mention}', inline=False)
        embed.set_author(name='Performance', icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/ping.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return