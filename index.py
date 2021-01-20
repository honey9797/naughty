import discord
from discord.ext import commands
import asyncio
from itertools import cycle
client = commands.Bot(command_prefix='!')

async def change_status():
    status = ['!help','Dani Daniel']



    await client.wait_until_ready()
    msg = cycle(status)

    while not client.is_closed():
        current_status = next(msg)
        await client.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(5)
@client.event
async def on_ready():
 print('Bot is ready')
client.remove_command('help')
@client.event
async def on_reaction_add(reaction,user):
    channel=reaction.message.channel
    await channel.send("{} has added {} to the message {}".format(user.name,reaction.emoji,reaction.message.content))
@client.event
async def on_reaction_remove(reaction,user):
    channel = reaction.message.channel
    await channel.send("{} has removed {} from the message {}".format(user.name, reaction.emoji, reaction.message.content))






@client.command()
async def status (ctx):
    await ctx.send("Hello i am under development")
    print("Hello i am under development")

@client.command()
async def ayush(ctx):
    await ctx.send("Chutiya hai bc")

@client.command()
async def manmode(ctx):
    await ctx.send("bhok mein ja bc")
@client.command()
async def honey(ctx):
    await ctx.send ("honey toh dev manus hai")

@client.command()
async def sagar(ctx):
    await ctx.send ("chutiya hai bc")
@client.command(pass_command=True)
async def help(ctx):
    author = ctx.message.author
    channel = ctx.message.channel
    embed =discord.Embed(
        description="Here are some useful commands list",
        colour= discord.Colour.gold()
    )

    embed.set_footer(text="Have a great time in my server")
    embed.set_author(name="Help")
    embed.add_field(name='Ayush',value='!ayush',inline='False')
    embed.add_field(name='Honey',value='!honey',inline='False')
    embed.add_field(name='Manmode',value='!manmode',inline='False')
    embed.add_field(name='Sagar',value='!sagar',inline='False')
    embed.add_field(name='Status',value='!status',inline='False')
    embed.add_field(name='Info',value='!embed',inline='False')
    await channel.send(embed=embed)
    await author.send(embed=embed)


@client.command(pass_context=True)
async def embed(ctx ):
    channel = ctx.message.channel
    embed = discord.Embed(

        description="You can watch the movie or porn \n You can also play the songs",
        colour=discord.Colour.dark_blue()
    )
    embed.set_footer(text='Have a great time in my server')
    embed.set_author(name='Kartikeya Choudhari')
    await channel.send(embed=embed)

@client.command()
async def logout(ctx):
    channel = ctx.message.channel

    await channel.send("I am signing out")
    await client.logout()

client.loop.create_task(change_status())
client.run("Nzk1MTg3MDU0NTcyNzMyNDI3.X_Ftpw.vEV2_fsKZ717o3O_7ipRTt8B7qM")