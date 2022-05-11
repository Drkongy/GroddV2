import os, importlib, discord
from turtle import done

class BananaHandler:
    
    def __init__(self, folder) -> None:
        self.folder = folder
        self.files = []
        self.Bananacommands = dict()
        list_files = os.listdir(folder)
        if 'BananaHandler.py' in list_files:
            list_files.remove('BananaHandler.py')
        for file in list_files:
            if file.endswith('.py'):
                self.files.append(file)

    def load_comands(self):
        for BananaCommand in self.files:
            BananaCommand = BananaCommand.split('.')[0]
            
            self.comands.Bananacommands[BananaCommand] = importlib.import_module(f'{self.folder.split("/")[-1]}.{BananaCommand}').BananaCommand
            print(f'[BananaHandler] Loaded {self.Bananacommands[BananaCommand].name}')





    async def execute_command(self, BananaCommand, args, message, client, db):
        if BananaCommand in self.Bananacommands:
            await self.Bananacommands[BananaCommand].main(args, message, client, db)
        else:
            embed = discord.Embed(title='Invalid Command ❌', description='Please use correct Arguments / Commands from !help', color=0xff0000)
            embed.set_author(name='ERROR', icon_url=message.author.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)


    





        

        
    
    