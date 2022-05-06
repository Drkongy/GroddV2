import discord
class Command:
    name = 'github'
    description = 'Sends you to the github repository'
    usage = 'github<No args>'

    async def main(args, message, client, db):
        embed = discord.Embed(title='Github', description='Click the link to go to the github repository' ,url='https://github.com/drkongy', color=0x00ff00)
        embed.set_author(name='Github', icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://www.kongolian.tech/Images/Icon3.png')
        embed.set_image(url = "https://img.bruzu.com/?bg=%23162230&h=500&w=500&a.tp=image&a.x=250&a.y=126&a.w=460&a.h=460&a.sx=0.4&a.sy=0.4&a.circleFrame=true&a.src=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F80266694%3Fv%3D4&b.tp=textbox&b.x=250&b.y=273&b.w=416&b.h=56&b.c=%23ffffff&b.t=Zeeshan&b.ta=center&b.fs=50&b.lh=1&b.fw=700&b.ff=Montserrat&b.maxHeight=50&c.tp=textbox&c.x=250&c.y=317&c.w=416&c.h=23&c.c=%238c8c8c&c.t=%40Drkongy&c.ta=center&c.fs=20&c.lh=1&c.fw=400&c.ff=Inter&c.maxHeight=20&d.tp=textbox&d.x=42&d.y=411&d.w=83&d.h=68&d.c=%23ffffff&d.t=8&d.ta=center&d.fs=60&d.lh=1&d.fw=900&d.ff=Inter&d.ox=left&d.maxHeight=60&e.tp=textbox&e.x=250&e.y=410&e.w=83&e.h=68&e.c=%23ffffff&e.t=7&e.ta=center&e.fs=60&e.lh=1&e.fw=900&e.ff=Inter&e.maxHeight=60&f.tp=textbox&f.ox=right&f.x=459&f.y=411&f.w=83&f.h=68&f.c=%23ffffff&f.t=11&f.ta=center&f.fs=60&f.lh=1&f.fw=900&f.ff=Inter&f.maxHeight=60&g.tp=textbox&g.x=83&g.y=452&g.w=127&g.h=23&g.c=%23ffffff&g.t=Followers&g.ta=center&g.fs=20&g.lh=1&g.fw=400&g.ff=Inter&g.maxHeight=500&h.tp=textbox&h.x=417&h.y=453&h.w=127&h.h=23&h.c=%23ffffff&h.t=Repositories&h.ta=center&h.fs=20&h.lh=1&h.fw=400&h.ff=Inter&h.maxHeight=500&i.tp=textbox&i.x=250&i.y=454&i.w=127&i.h=23&i.c=%23ffffff&i.t=Following&i.ta=center&i.fs=20&i.lh=1&i.fw=400&i.ff=Inter&i.maxHeight=500&j.tp=image&j.x=437&j.y=61&j.w=496&j.h=512&j.sx=0.16&j.sy=0.15&j.src=https%3A%2F%2Fi.ibb.co%2Ffrv5pB3%2Fgithub-logo.png")
        embed.set_footer(text='Made by Zeeshan & Kai')
        await message.channel.send(embed=embed)
        return