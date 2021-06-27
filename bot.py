import discord
import os 
from discord.ext import commands

bot = commands.Bot(command_prefix="+")


@bot.event
async def on_ready():
    print(f"{bot.user} has logged in ")
    bot.load_extension('cogs.music')
    

bot.remove_command("help")

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name="❓HELP-COMANDS❓")
    embed.add_field(name="🎵Music🎵", value="+p to play some music\n+pause to pause the music\n+stop to turn off the music\n+skip to play the next song\n+previous to see the next song\n+shuffle to do a mix\n+repeat to listen another time the same song\n+q to see the queue", inline=False)
    embed.add_field(name="⚒Login⚒", value="+join to enter the bot into a channel\n+bye to disconnect the bot", inline=False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/432254865859805194/748337132921290802/limon_1.jpg")

    await ctx.send(author, embed=embed)

bot.run("Nzg5NDc2MjgyMDg0NjIyNDA3.X9ynFQ.E_yCDCr-jIg3GircSmU_7HVizp4")
