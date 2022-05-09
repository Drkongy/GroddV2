import discord, config
from lowdb import Low, File


class Command:
    name = 'prefix'
    description = 'Allows you to change the prefix'
    usage = 'prefix<Prefix>'
    

    async def main(args, message, client, db):
        FileAdapter = File('./Databases/db.json')
        prefixDB = Low(FileAdapter) 
        if len(args) > 0:
            prefix = args[0]
            prefixDB.set(f'Guilds.${message.guild.id}.Prefix', prefix) # Returns self, so that you can use .write() to write to json
            prefixDB.write() # Writes memory to json
            #call the init function
            

           
            
            #reload the bot
            print(f'[Prefix] Changed prefix to {prefix}')
            embed = discord.Embed(title='Prefix changed! ✅', description='The new prefix is: ' + prefix, color=0x00ff00)
            embed.set_author(name='Prefix', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon3.png')
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            

        else:
            prefix = prefixDB.get(f'Guilds.${message.guild.id}.Prefix')
            embed = discord.Embed(title='Prefix', description='The current prefix is: ' + prefix, color=0x00ff00)
            embed.set_author(name='Prefix', icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon3.png')
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)
            return
            # await message.channel.send("test")
            # return

    


    def get_prefix(self, guild):
        FileAdapter = File('./Databases/db.json')
        prefixDB = Low(FileAdapter)
        prefix = prefixDB.get(f'Guilds.${guild}.Prefix')
        return prefix

