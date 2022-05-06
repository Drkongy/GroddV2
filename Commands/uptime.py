import discord, time
class Command:
    name = 'uptime'
    description = 'Shows the uptime of the bot'
    usage = 'uptime<No Args>'
    start_time = time.time()


    async def main(args, message, client, db):
        uptime = time.time() - Command.start_time
        days = int(uptime // 86400)
        hours = int(uptime // 3600 % 24)
        minutes = int(uptime // 60 % 60)
        seconds = int(uptime % 60)
        uptime = f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds'
        embed = discord.Embed(color=0x000000)
        embed.set_author(name='Zeeshan', icon_url=message.author.avatar_url)
        embed.add_field(name='Uptime:', value=uptime, inline=False)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/Clock.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        print(f'[Uptime]  :: {uptime}')
        return


 


        