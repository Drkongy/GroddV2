import discord
class Command:
    name = 'serverinfp'
    description = 'shows infomation about the server'
    usage = 'serverinfo<No Args>'


    async def main(args, message, client, db):
        embed = discord.Embed(color=0x000000)
        embed.set_author(name='Zeeshan', icon_url=message.author.avatar_url)
        embed.add_field(name='Server Name:', value=message.guild.name, inline=False)
        embed.add_field(name='Server ID:', value=message.guild.id, inline=False)
        embed.add_field(name='Server Owner:', value=message.guild.owner, inline=False)
        embed.add_field(name='Server Region:', value=message.guild.region, inline=False)
        embed.add_field(name='Server Created At:', value=message.guild.created_at, inline=False)
        embed.add_field(name='Server Member Count:', value=message.guild.member_count, inline=False)
        embed.add_field(name='Server Channel Count:', value=len(message.guild.channels), inline=False)
        embed.add_field(name='Server Role Count:', value=len(message.guild.roles), inline=False)
        embed.add_field(name='Server Embed Channel Count:', value=len(message.guild.text_channels), inline=False)
        embed.add_field(name='Server Voice Channel Count:', value=len(message.guild.voice_channels), inline=False)
        embed.add_field(name='Server Emoji Count:', value=len(message.guild.emojis), inline=False)
        embed.add_field(name='Server Category Count:', value=len(message.guild.categories), inline=False)
        embed.add_field(name='Server Boost Tier:', value=message.guild.premium_tier, inline=False)
        embed.add_field(name='Server Boost Subscription:', value=message.guild.premium_subscription_count, inline=False)
        embed.add_field(name='Server Boosts:', value=message.guild.premium_subscription_count, inline=False)
        embed.add_field(name='Server Boosts Until:', value=message.guild.premium_subscription_count, inline=False)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/icon10.png')
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)



        