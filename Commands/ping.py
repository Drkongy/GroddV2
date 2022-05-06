import discord, time
class Command:
    name = 'ping'
    description = 'gets the ping of the discord bot'
    usage = 'ping<No Args>'


    async def main(args, message, client, db):
        #get api ping in milliseconds
        api_ping = client.latency * 1000
        api_ping = int(api_ping)

        websocket_ping = (time.time() - message.created_at.timestamp())
        websocket_ping = int(websocket_ping)
        #get total ping in milliseconds
        total_ping = api_ping + websocket_ping

        embed = discord.Embed(color=0x000000)
        embed.set_author(name='Zeeshan', icon_url=message.author.avatar_url)
        embed.add_field(name='API Ping:', value=f'{api_ping}ms', inline=False)
        embed.add_field(name='Web Socket Ping:', value=f'{websocket_ping}ms', inline=False)
        embed.add_field(name='General Ping:', value=f'{total_ping}ms', inline=False)


        embed.set_thumbnail(url='https://www.kongolian.tech/Images/ping.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return

        