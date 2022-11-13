import discord
from discord.ext import commands
from private.config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)


# Ready Event
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Made by Plux2", url='https://discord.gg/jAV5pBW4tT'))
    print("|---------------------------------------|")
    print(f' Bot Online | {bot.user} ')
    print("|---------------------------------------|")


# Join Message
@bot.event
async def on_member_join(member):
    print(f'Member join: {member.mention}')
    embed = discord.Embed(title="A new member has joined the server!",
                          description=f"That's insane {member.mention} joined the server that's insane.",
                          color=0xae00ff)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1036662749830328360/1037867554489778186/Waffle_House_Esports_Logo_125x125.png")
    embed.set_footer(text="Made by Plux2")
    await bot.get_channel(1036388767340179539).send(embed=embed)


# Leave Message
@bot.event
async def on_member_remove(member):
    print(f'Member leave: {member.name}')
    embed = discord.Embed(title="Member has left the server",
                          description=f"{member.mention} left the server... good thing I put a fentanyl in their drink.",
                          color=0xae00ff)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1036662749830328360/1037867554489778186/Waffle_House_Esports_Logo_125x125.png")
    embed.set_footer(text="Made by Plux2")
    await bot.get_channel(1036388767340179539).send(embed=embed)


# Commands

# Rules Command
@bot.command()
@commands.has_permissions(administrator=True)
async def rules(ctx):
    embed = discord.Embed(title="‎ ")
    embed.set_author(name="SCS DISCORD SERVER RULES",
                     icon_url="https://media.discordapp.net/attachments/955885405574680696/955888224243441684"
                              "/download.jpg")
    embed.add_field(name="Rule 1: Be Respectful!",
                    value="Please respect all users, regardless of your liking towards them in person, you can just "
                          "block said person or ignore them. This also means no threats and DDoSing. I don't care "
                          "that you are a quirky hacker.",
                    inline=True)
    embed.add_field(name="Rule 2: No spamming!",
                    value="Please don't spam anyone in dms, in chat, whatever. It's very annoying and makes you "
                          "unpleasant to speak to. This also applies to vc's; Don't eat your microphone just to be "
                          "annoying.",
                    inline=True)
    embed.add_field(name="Rule 3: No NSFW material!",
                    value="I know you all are immature middle schoolers but please keep the wack stuff to your own "
                          "server.",
                    inline=True)
    embed.add_field(name="DISCLAIMERS:",
                    value="The Admins and Mods will Mute/Kick/Ban per discretion. If you feel mistreated dm "
                          "@Moderators and we will resolve the issue.  All Channels will have 'channel info'. ⬇️ On "
                          "PC/Mac look to the top of the Discord window to the right of the channel label. (AKA the "
                          "general or rules) On Mobile look to the top of your screen in the chat window and click on "
                          "the channel label (AKA the general or rules). That will bring you to the members list "
                          "menu. Look below the channel label.  Your presence in this server implies accepting these "
                          "rules. If you break a rules you will be kicked out of the server and banished for "
                          "LIFE!!!1! If you don't read them and you break a rule that's on you.",
                    inline=True)
    embed.set_footer(text="SCS DISCORD SERVER LINK: https://discord.gg/e7uQYh64hn")
    await ctx.send(embed=embed)


# Purge Command
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
    print(f"Purge ({limit}) command executed successfully.")
    await ctx.channel.purge(limit=limit)
    await ctx.message.delete()


# Missing Perms Error
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        print('Command failed: incorrect permissions.')
        await ctx.send("you cant use that command dumbass lmfao")


bot.run(TOKEN)