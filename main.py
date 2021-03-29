from discord.ext import commands
import discord
import os

from cogs.cgo.utils import get_random_cgo_quote

TOKEN = os.getenv("BOT_TOKEN")
INTENTS = discord.Intents.default()
PREFIX = ">"

bot = commands.Bot(
    guild_subscriptions=True,
    intents=INTENTS,
    command_prefix=PREFIX
)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.event
async def on_message(message):
    """
    Function executed on each message received
    """
    if bot.user in message.mentions:
        quote = get_random_cgo_quote()
        embed = discord.Embed(
            title="CGO once said:",
            description=quote
        )
        file = discord.File("cgo.jpg")
        embed.set_image(url="attachment://cgo.jpg")

        await message.channel.send(file=file, embed=embed)

@bot.event
async def on_command_error(ctx, error):
    """
    Function executed on each command error made
    """
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I believe you totally failed your command")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("I believe you forgot something important in your command :thinking:")
    if isinstance(error, (commands.CheckFailure, commands.MissingPermissions)):
        await ctx.send("I believe you cannot use that")
    if isinstance(error, discord.Forbidden):
        await ctx.send("Stop asking me to do something I cannot")

if __name__ == "__main__":
    bot.run(TOKEN)
