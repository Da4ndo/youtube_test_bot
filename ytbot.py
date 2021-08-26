TOKEN = open("token.txt", "r", encoding='utf-8').read()
#GET THE TOKEN

import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands import *
import datetime
import glob
from discord_slash import SlashCommand
from discord_components import DiscordComponents, Button, ButtonStyle
## DEFAULT IMPORTS

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print("Logged in as {0} ({0.id})".format(bot.user))
    DiscordComponents(bot)

## CODE GOING HERE

print("Auto Cog Loader...\nLoaded Cogs:")
for file in glob.glob("cogs/*.py"):
    cog = file.replace("\\", ".").replace(".py", "")
    bot.load_extension(cog)
    print(f"\t{cog}")

## YEAHH
bot.run(TOKEN)