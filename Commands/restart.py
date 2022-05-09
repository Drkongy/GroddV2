import discord, config, sys, os
class Command:
    name = 'restart'
    description = 'Restarts the discord bot'
    usage = 'restart<user>'



    async def main(args, message, client, db):

        #make an embed
        embed = discord.Embed(title='Restarting...', description='Restarting the bot...', color=0x00ff00)
        embed.set_author(name='Zeeshan', icon_url=message.author.avatar_url)
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return

            
       





        
 


        