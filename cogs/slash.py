from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash.context import SlashContext
import discord
from discord.ext import commands
import time

class SlashParancsok(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test2(self, ctx, ember:discord.Member, reason=""):
        await ctx.send(f"Valid {ember.mention}!  --> {reason}")

    @cog_ext.cog_slash(name="test2", description="Ezzel a parancsal tesztelsz engem.", guild_ids=[874569663416258600],
    options=[
        create_option(
            name="ember",
            description="Ping a member",
            option_type=6,
            required=True
        ),
        create_option(
            name="reason",
            description="asd",
            option_type=3,
            required=False,
            choices=[
                create_choice(name="hack", value="Mert hackelt."),
                create_choice(name="Nem szeretem", value="Már nem szeretem.")
            ]
        )
        ]
    
    )
    async def _test2(self, *args, **kwargs):
        time.sleep(5)
        await self.test2(*args, **kwargs)

def setup(bot):
    bot.add_cog(SlashParancsok(bot))