import os, importlib, discord
from turtle import done

class BananaHandler:
    def __init__(self, folder) -> None:
        # make an args handler for the commands for bananahandler
        self.folder = folder
        self.files = []
        self.commands = dict()
        list_files = os.listdir(folder)
        if 'BananaHandler.py' in list_files:
            list_files.remove('BananaHandler.py')
        for file in list_files:
            if file.endswith('.py'):
                self.files.append(file)
        
    def load_comands(self):
        for command in self.files:
            command = command.split('.')[0]
            self.commands[command] = importlib.import_module(f'{self.folder.split("/")[-1]}.{command}').BananaCommand

    def print(self):
        for command in self.files:
            command = command.split('.')[0]
            self.commands[command] = importlib.import_module(f'{self.folder.split("/")[-1]}.{command}').BananaCommand
            print(f'[BananaHandler] Loaded {self.commands[command].name}')


    async def execute_command(self, command, args, message, client, db):
        #check all the commands aliases 
        try:
            for command_name in self.commands:
                for alias in self.commands[command_name].aliases:
                    if command in self.commands[command_name].aliases:
                        command = self.commands[command_name].name
                        break
        except:
            pass


        if command in self.commands:
            await self.commands[command].main(args, message, client, db)
        else:
            embed = discord.Embed(title='Invalid Command ❌', description='Please use correct Arguments / Commands from !help', color=0xff0000)
            embed.set_author(name='ERROR', icon_url=message.author.avatar_url)
            embed.set_footer(text='Made by Zeeshan & Kai')
            await message.channel.send(embed=embed)


    



    
    