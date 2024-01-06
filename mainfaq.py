import discord
from discord.ext import commands

# This class holds the main FAQ commands
class MainFAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    