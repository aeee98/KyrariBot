import discord
from discord.ext import commands
import os
from dotenv import dotenv_values
import logging
import logging.handlers
import asyncio
from typing import Literal, Optional
import util

#KyrariBot is designed as a fast helper to the Princess Connect Discord.
class KyrariBot(commands.Bot):
    async def setup_hook(self):
        await client.load_extension("mainfaq")
        await client.load_extension("eka")
        await client.load_extension("viral")

# Setup
config = dotenv_values(".env")
intents = discord.Intents.default()
client = KyrariBot(command_prefix="k!", intents=discord.Intents(messages=True, message_content=True, guild_messages=True, emojis_and_stickers = True, typing = True), application_id=config.get("APPLICATION_ID"))

#DEBUG LOGGING
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

@client.event
async def on_ready():
    print("Bot is ready")


#Default Sync Command. Only used by bot owner. Source of function: https://about.abstractumbra.dev/discord.py/2023/01/29/sync-command-example.html
@client.command()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

# This function is used to check for an announcement/general channel where the developer can send a message to announce new features on the fly.
@client.command()
@commands.is_owner()
async def check(ctx: commands.Context) -> None:
    for guild in client.guilds:
        text_to_send_back = "Server " + guild.name + " possible announcement channels: "
        for channel in guild.channels:
            if ('general' in channel.name or 'announcement' in channel.name or 'bot' in channel.name):
                text_to_send_back += channel.name + " " 
        ctx.send(text_to_send_back)


@client.command()
async def firsttest(ctx):
    await ctx.send("Hi")

# Main Method
async def main():
    util.populate_dict_from_db()
    async with client:
        await client.start(config.get("BOT_ID"))
    
asyncio.run(main())