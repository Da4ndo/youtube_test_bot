import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands import *
from discord_components import DiscordComponents, Button, ButtonStyle

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.reply("Test")
    
    @commands.command()
    async def button(self, ctx):
        await ctx.send(content="Válasz!", components=[
            Button(style=ButtonStyle.green, label="1", custom_id="button1"),
            Button(style=ButtonStyle.gray, label="2", custom_id="button2"),

        ])
    
    @commands.Cog.listener()
    async def on_button_click(self, interaction):
        if interaction.component.custom_id == "button1":
            await interaction.respond(type=7, content="ASD")
        
        elif interaction.component.custom_id == "button2":
            await interaction.edit_origin(content="AD")
    

def setup(bot):
    bot.add_cog(Test(bot))