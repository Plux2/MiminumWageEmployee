import discord
import random
from discord.ext import commands
from alexlist import list1
from os import environ
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)
load_dotenv()
TOKEN = environ["TOKEN"]


@bot.event
async def on_ready():
    print("|---------------------------------------|")
    print(f' Bot Online | {bot.user} ')
    print("|---------------------------------------|")


@bot.command()
async def gus(ctx):
    print('.gus successfully executed')
    await ctx.send(f'<@830851686976978984> https://tenor.com/view/siploxt-sans-ass-sexy-ass-gif-21685897')


@bot.command()
async def alex(ctx):
    if ctx.channel.id == 1036662749830328360:
        print('.alex successfully executed')
        await ctx.send(random.choice(list1))
    else:
        await ctx.send('you cannot use this command here lol')


@bot.event
async def on_member_join(member):
    print(f'Member join: {member.mention}')
    embed = discord.Embed(title="A new member has joined the server!",
                          description=f"That's insane {member.mention} joined the server that's insane.", color=0xae00ff)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1036662749830328360/1037867554489778186/Waffle_House_Esports_Logo_125x125.png")
    embed.set_footer(text="Made by Plux2")
    await bot.get_channel(1036388767340179539).send(embed=embed)


@bot.event
async def on_member_remove(member):
    print(f'Member leave: {member.name}')
    embed = discord.Embed(title="Member has left the server",
                          description=f"{member.mention} left the server... good thing I put a fentanyl in their drink.", color=0xae00ff)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1036662749830328360/1037867554489778186/Waffle_House_Esports_Logo_125x125.png")
    embed.set_footer(text="Made by Plux2")
    await bot.get_channel(1036388767340179539).send(embed=embed)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
        print(f"Purge ({limit}) command executed successfully.")
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        print('Command failed: incorrect permissions.')
        await ctx.send("you cant use that command dumbass lmfao")



bot.run(TOKEN)