import discord, datetime, time, asyncio, os, json, random, requests, aiohttp
import colorama
from discord.ext import commands
from datetime import datetime
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from pytz import timezone
from random import choice
from discord import Webhook, AsyncWebhookAdapter
from colorama import Fore, Back, Style
from discord.ext.commands import has_permissions, CheckFailure
from datetime import datetime
import ctypes


colorama.init()
version = "2.4"
prefix = "?"
SecondVersion = version
ctypes.windll.kernel32.SetConsoleTitleW(f'Bread Bot  | Version {version} | Loading...')

determine_flip = [1, 0]
bot = commands.Bot(command_prefix='?', case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    print(f'''{Fore.RESET}{Fore.MAGENTA}
                         ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
                        █  ▄    █   ▄  █ █       █      █      █   █  ▄    █       █       █
                        █ █▄█   █  █ █ █ █    ▄▄▄█  ▄   █  ▄    █  █ █▄█   █   ▄   █▄     ▄█
                        █       █   █▄▄█▄█   █▄▄▄█ █▄█  █ █ █   █  █       █  █ █  █ █   █  
                        █  ▄   ██    ▄▄  █    ▄▄▄█      █ █▄█   █  █  ▄   ██  █▄█  █ █   █  
                        █ █▄█   █   █  █ █   █▄▄▄█  ▄   █       █  █ █▄█   █       █ █   █  
                        █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█▄█ █▄▄█▄▄▄▄▄▄█   █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█  
                                                                         
                                                 
{Fore.BLUE}                                       Logged in as | {Fore.CYAN}{bot.user.name}#{bot.user.discriminator}
{Fore.BLUE}                                             Prefix | {Fore.CYAN}{prefix}
{Fore.BLUE}                                             Version| {Fore.CYAN}{version}
{Fore.BLUE}                                                   Made by Scxred#8967
  
    '''+Fore.RESET)

    ctypes.windll.kernel32.SetConsoleTitleW(f'Bread Bot  | Version {SecondVersion} |  {bot.user.name}#{bot.user.discriminator} ')


@bot.command()
async def serverpfp(ctx):
    embed = discord.Embed(title=ctx.guild.name)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
        embed = discord.Embed(title=f"Pong {bot.latency}ms latency")
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def logout(ctx):
    await ctx.send('Logging out.')
    await ctx.bot.logout()
    print (Fore.GREEN + f"{bot.user.name} has logged out successfully." + Fore.RESET)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)

async def purge(ctx, limit: int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)
        await ctx.send(f'purged {limit} messages')
        await ctx.message.delete()


@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, message=None):
        await ctx.message.delete()
        bred = discord.Embed(title="BreadBot :D 🍞", description=f"{message}")
        await ctx.send(embed=bred)




@bot.event  
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('This command is on cooldown, you can use it in {round(error.retry_after, 2)}')

@purge.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")



@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    mention = []
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name="Nickname:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def version(ctx):
        embed = discord.Embed(title="Version | BreadBot :D 🍞", description=f"{ctx.author.mention} Im on version {version}")
        await ctx.send(embed=embed)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def getpfp(ctx, member: Member = None):
 if not member:
  member = ctx.author
 await ctx.send(member.avatar_url)



@bot.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send(f"Prefix changed to ``{prefix}``")


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"[Complete] Removed {passed} messages with {failed} fails")

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user) 
    await ctx.send(f"{user}, Has Been unbanned")

@bot.command(description="bans a user with specific reason (only admins)") #ban
@commands.has_permissions(administrator=True)
async def ban (ctx, member:discord.User=None, reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot ban yourself!""") 
    else:
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        print(member)
        print(reason)
        await ctx.channel.send(f"{member} is banned!")
 except:
    await ctx.send(f"Error banning user {member} (cannot ban owner or   staff members above my roles.)")



@bot.command(pass_context=True)
async def test(ctx):
    await ctx.send(f":bread: {ctx.message.author.mention} Im online:bread: ")







@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=True
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="Nope.",
            value="Don't think I got that command, boss!"
        )

    await ctx.send(embed=help_embed)

@bot.command(pass_context=True)
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip | BreadBot :D 🍞", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip | BreadBot :D 🍞", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!")
        await ctx.send(embed=embed)




@bot.command()
async def serverinfo(ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f'{guild} Info', description="Coded by Scxred#8967",
                          timestamp=ctx.message.created_at, color=discord.Color.red())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="Number of channels:", value=len(guild.channels))
        embed.add_field(name="Number of roles:", value=len(guild.roles))
        embed.add_field(name="Number of boosters:", value=guild.premium_subscription_count)
        embed.add_field(name="Number of users:", value=guild.member_count)
        embed.add_field(name="Date created:", value=guild.created_at)
        embed.add_field(name="Server owner:", value=guild.owner)
        embed.set_footer(text=f"{ctx.author} used serverinfo command.", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def bonk(ctx):
    
    await ctx.send("https://tenor.com/view/bonk-gif-18805247")



@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send(":bread: You did not mention a channel!:bread: ")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("bread:bread: ")
        await ctx.send("bread:bread: ")

    else:
        await ctx.send(f"No channel named {channel.name} was found!")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f":bread: yo {member.name}, Welcome! :D:bread: ")


# Animals
@bot.command()
async def bird(ctx,description="Sends a photo of a bird"):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/bird')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/bird')
      factjson = await request2.json()

   embed = discord.Embed(title="Birdo", icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024', color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text="BreadBot",icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024')
   await ctx.send(embed=embed)

@bot.command()
async def fox(ctx,description="Sends a photo of a Fox"):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/fox')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/fox')
      factjson = await request2.json()

   embed = discord.Embed(title="Foxy🍞", icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024', color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text="BreadBot",icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024')
   await ctx.send(embed=embed)

@bot.command()
async def panda(ctx,description="Sends a photo of a Panda"):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/panda')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/panda')
      factjson = await request2.json()

   embed = discord.Embed(title="Panda!🍞", icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024', color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text="BreadBot",icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024')
   await ctx.send(embed=embed)


@bot.command()
async def cat(ctx,description="Sends a photo of a Cat"):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/cat')
      factjson = await request2.json()

   embed = discord.Embed(title="Cat🍞", icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024', color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text="BreadBot",icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024')
   await ctx.send(embed=embed)

@bot.command()
async def dog(ctx,description="Sends a photo of a Dog"):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

   embed = discord.Embed(title="Doggo🍞", icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024', color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text="BreadBot",icon_url='https://cdn.discordapp.com/avatars/816932049284890655/d80e9c79176998c8d22af2d59d59084e.png?size=1024')
   await ctx.send(embed=embed)

bot.run("TOKEN")