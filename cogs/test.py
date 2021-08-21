import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands import *

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.reply("Test")

def setup(bot):
    bot.add_cog(Test(bot))