import random

import interactions

from private.config import TOKEN

bot = interactions.Client(token=TOKEN)


# Ready Event
@bot.event()
async def on_ready():
    print(f'Bot is online | Minimum Wage Employee#2169')


# Join Message
@bot.event
async def on_member_join(member):
    print(f'Member join: {member.mention}')
    embed = interactions.Embed(title="A new member has joined the server!",
                               description=f"That's insane {member.mention} joined the server that's insane.",
                               color=0xae00ff)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1036662749830328360/1037867554489778186"
            "/Waffle_House_Esports_Logo_125x125.png")
    embed.set_footer(text="Made by Plux2")
    await bot.get_channel(1036388767340179539).send(embed=embed)


# Leave Message
@bot.event
async def on_member_remove(member):
    print(f'Member leave: {member.name}')
    embed = interactions.Embed(title="Member has left the server",
                               description=f"{member.mention} left the server... good thing I put a fentanyl in their "
                                           f"drink.",
                               color=0xae00ff)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1036662749830328360/1037867554489778186"
            "/Waffle_House_Esports_Logo_125x125.png")
    embed.set_footer(text="Made by Plux2")
    await bot.get_channel(1036388767340179539).send(embed=embed)


# WHE DISCORD RULES
@bot.command(
    name="wherules",
    description="Waffle House Esports Official Discord Server Rules",
    scope=1036049676669030460
)
async def rules(ctx: interactions.CommandContext):
    embed = interactions.Embed(title="‎ ")
    embed.set_author(name="WAFFLE HOUSE ESPORTS RULES",
                     icon_url="https://cdn.discordapp.com/attachments/1038226171537670164/1042604781383974993"
                              "/Waffle_House_Esports_Logo_125x125.png")
    embed.add_field(name="RULE 1:",
                    value="be nice! here at waffle house esports, we have a ZERO TOLERANCE policy for being a BIG OL' "
                          "MEANY BUTT HEAD....... it also goes without saying that discriminating against other's "
                          "race, gender, sexual orientation, opinions, or other characteristics is not good. if "
                          "someone is being mean, ping @FOUNDER or directly contact either me or @Plux2!",
                    inline=False)
    embed.add_field(name="RULE 2:",
                    value="no overly nsfw media and no extremely nsfw discussion! ping me or @Plux2 or @FOUNDER if "
                          "someone is posting silly things that are nsfw!",
                    inline=False)
    embed.add_field(name="RULE 3:",
                    value="no super political discussion please! due to media polarization, respectful political "
                          "discussion is rare hard to conduct outside of specifically politically focused "
                          "environments. like rule 2, if you can talk about it without pushing the boundary, "
                          "we mods will not do anything.",
                    inline=False)
    embed.add_field(name="RULE 4:",
                    value="don't be overly shitposty in channels that are not media! you can post memes in general, "
                          "but don't post too many in a short period of time.",
                    inline=False)
    embed.add_field(name="RULE 5:",
                    value="don't break the discord TOS! also don't do anything illegal in this server like leak other "
                          "people's information, and preferably don't leak your own personal information! ",
                    inline=False)
    embed.set_footer(text="Made by Plux2")
    await ctx.send(embeds=embed)


# SCS DISCORD RULES
@bot.command(
    name="scsrules",
    description="SCS Official Discord rules",
    scope=920810071296966696
)
async def rules1(ctx: interactions.CommandContext):
    embed = interactions.Embed(title="‎")
    embed.set_author(name="SCS DISCORD SERVER RULES",
                     icon_url="https://media.discordapp.net/attachments/955885405574680696/955888224243441684"
                              "/download.jpg")
    embed.add_field(name="Rule 1: Be Respectful!",
                    value="Please respect all users, regardless of your liking towards them in person, you can just "
                          "block said person or ignore them. This also means no threats and DDoSing. I don't care "
                          "that you are a quirky hacker.",
                    inline=False)
    embed.add_field(name="Rule 2: No spamming!",
                    value="Please don't spam anyone in dms, in chat, whatever. It's very annoying and makes you "
                          "unpleasant to speak to. This also applies to vc's; Don't eat your microphone just to be "
                          "annoying.",
                    inline=False)
    embed.add_field(name="Rule 3: No NSFW material!",
                    value="I know you all are immature middle schoolers but please keep the wack stuff to your own "
                          "server.",
                    inline=False)
    embed.add_field(name="DISCLAIMERS:",
                    value="The Admins and Mods will Mute/Kick/Ban per discretion. If you feel mistreated dm "
                          "@Moderators and we will resolve the issue.  All Channels will have 'channel info'. ⬇️ On "
                          "PC/Mac look to the top of the Discord window to the right of the channel label. (AKA the "
                          "general or rules) On Mobile look to the top of your screen in the chat window and click on "
                          "the channel label (AKA the general or rules). That will bring you to the members list "
                          "menu. Look below the channel label.  Your presence in this server implies accepting these "
                          "rules. If you break a rules you will be kicked out of the server and banished for "
                          "LIFE!!!1! If you don't read them and you break a rule that's on you.",
                    inline=False)
    embed.set_footer(text="SCS DISCORD SERVER LINK: https://discord.gg/e7uQYh64hn")
    await ctx.send(embeds=embed)


# Purge Command
@bot.command(
    name='purge',
    description='Deletes a number of above messages (Admin only)',
    default_member_permissions=interactions.Permissions.MANAGE_MESSAGES,
    options=[
        interactions.Option(
            name="amount",
            description="Amount of deleted messages",
            type=interactions.OptionType.INTEGER,
            required=True,

        ),
    ],
)
async def purge(ctx: interactions.CommandContext, amount: interactions.OptionType.INTEGER):
    print(f"Purge ({amount}) command executed successfully.")
    await ctx.get_channel()
    await ctx.channel.purge(amount=amount)
    await ctx.send(f'Purged {amount} messages.', ephemeral=True)


@bot.command(
    name='presence',
    description='changes bot presence (Admin only)',
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
)
async def presence(ctx: interactions.CommandContext):
    list1 = [
        'video games with my friends',
        'car soccer',
        'alex simulator (being stupid simulator)',
        'sully simulator (being awesome simulator)',
        'the waffle iron',
        'with hot wheel B)',
        'wtf (what the fracktivist)',
    ]
    status = random.choice(list1)
    print(f"Presence command executed successfully ({status})")
    await bot.change_presence(
        interactions.ClientPresence(
            status=interactions.StatusType.ONLINE,
            activities=[
                interactions.PresenceActivity(name=status, type=interactions.PresenceActivityType.GAME)
            ]
        )
    )
    await ctx.send(f'Status successfully changed to {status}', ephemeral=True)

bot.start()
