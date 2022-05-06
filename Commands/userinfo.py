import discord
class Command:
    name = 'userinfo'
    description = 'shows infomation about a user'
    usage = 'userinfo <user>'


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
            

            roles = ''
            #get current user infomation 
            embed = discord.Embed(color=0x000000)
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.add_field(name='ID:', value= user.id, inline=False)
            embed.add_field(name='Nickname:', value=user.nick, inline=False)
            embed.add_field(name='Status:', value=user.status, inline=False)
            embed.add_field(name='Joined At:', value=user.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
            embed.add_field(name='Created At:', value=user.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
            embed.add_field(name='Role Count:', value=len(user.roles), inline=False)
            for role in user.roles:
                roles += f'{role.name}\n'
            embed.add_field(name='Roles:', value=roles, inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return


        else:
            roles = ''
            #get current user infomation 
            embed = discord.Embed(color=0x000000)
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.add_field(name='ID:', value=message.author.id, inline=False)
            embed.add_field(name='Nickname:', value=message.author.nick, inline=False)
            embed.add_field(name='Status:', value=message.author.status, inline=False)
            embed.add_field(name='Joined At:', value=message.author.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
            embed.add_field(name='Created At:', value=message.author.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
            embed.add_field(name='Role Count:', value=len(message.author.roles), inline=False)
            for role in message.author.roles:
                roles += f'{role.name}\n'
            embed.add_field(name='Roles:', value=roles, inline=False)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return
        

            
    



        