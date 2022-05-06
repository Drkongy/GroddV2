import discord
class Command:
    name = 'avatar'
    description = 'Shows the avatar of the user'
    usage = 'avatar<user>'


    async def main(args, message, client, db):
        if len(args) > 0:
            string = args[0].replace('<@', '')
            string = string.replace('>', '')
            user = await message.guild.fetch_member(int(string))

            if user is None:
                embed = discord.Embed(title='User not found ❌', description='Please make sure you are typing the correct user!', color=0xff0000)
                embed.set_author(name='Zeeshan', icon_url=message.author.avatar_url)
                embed.set_footer(text='Made by Zeeshan & Kai')
                await message.channel.send(embed=embed)
                return

            embed = discord.Embed(color=0x000000)
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_image(url =user.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return
        else:
            embed = discord.Embed(color=0x000000)
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_image(url =message.author.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return





        
 


        