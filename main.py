import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import logging.handlers
from mainfaq import MainFAQ

# Setup
dotenv_path = os.join(os.dirname(__file__), '.env')
load_dotenv(dotenv_path)
intents = discord.Intents.default()
client = commands.Bot()
client.add_cog(MainFAQ(client))


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


# Main Method
def main():
    client.run(os.environ.get("BOT_ID"), log_handler=None)
    print("Client is Called. Starting Up")
    
# Run
if __name__ == "__main__":
    main()