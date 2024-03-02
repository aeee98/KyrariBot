import discord
from discord import app_commands
from discord.ext import commands
from dotenv import dotenv_values
from util import faq_dict, convert_time
import datetime

config = dotenv_values(".env")

# This class holds the main FAQ commands
class MainFAQ(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
       
    @app_commands.command(name="tierlist", description = "Sends a direct link to the tier list by Kyrari.")
    @app_commands.rename(private_value="hidden")
    @app_commands.describe(private_value="Choose yes if you only want to see if for yourself, and no if you want to send to the channel.")
    @app_commands.choices(private_value=[app_commands.Choice(name="yes", value = 1), app_commands.Choice(name="no", value=0)])
    async def tier_list(self, interaction: discord.Interaction, private_value: app_commands.Choice[int]) -> None:
        await interaction.response.send_message(config.get("SHEET_TIER_LIST_URL"), ephemeral = private_value.value == 1)

    #TODO : Make this a more dynamic solution since hardcoding is obviously not the way to go.
    #TODO : Turning below functions into a dynamic card
    @app_commands.command(name="gachaforecast", description="Sends you the link to the gacha forecast by Eka This message is private.")
    @app_commands.checks.cooldown(rate=1, per=1200)
    async def gacha_forecast(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(faq_dict["gachaforecast"], ephemeral = True)

    @app_commands.command(name="gachaguide", description="Sends you the link to the gacha guide by Eka. This message is private.")
    @app_commands.checks.cooldown(rate=1, per=1200)
    async def gacha_forecast(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(faq_dict["gachaguide"], ephemeral = True)

    @app_commands.command(name="prifes", description="Shows the priority list for all Prifes Banners by Kyrari. This message is private.")
    @app_commands.checks.cooldown(rate=1, per=1200)
    async def prifes_guide(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(faq_dict["prifes"], ephemeral = True)

    @app_commands.command(name="coinshop", description="Shows the priority list for all the currency shops by Wazahai. This message is private.")
    @app_commands.checks.cooldown(rate=1, per=1200)
    async def coinshop_guide(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(faq_dict["coinshop"], ephemeral = True)

    @app_commands.command(name="arenareset", description="Tells you when the next arena reset is. This message is private.")
    @app_commands.checks.cooldown(rate=1, per=1200)
    async def dailyreset(self, interaction: discord.Interaction) -> None:
        now = datetime.datetime.now(datetime.timezone.utc)
        # get the next closest 10am UTC+0 as this is the reset
        resettime = datetime.datetime(year=now.year, month=now.month, day = now.day, hour = 10, minute = 0,tzinfo=datetime.timezone.utc)
        if (resettime <= now):
            # add a day if past reset
            resettime += datetime.timedelta(days=1)
        
        secondsremaining = resettime - now
        message = "The PvP Reset is at 7PM JST. Time Remaining: " + convert_time(secondsremaining.total_seconds())
        await interaction.response.send_message(message,ephemeral=True)


    @app_commands.command(name="dailyreset", description="Tells you when the next daily reset is. This message is private.")
    @app_commands.checks.cooldown(rate=1, per=1200)
    async def dailyreset(self, interaction: discord.Interaction) -> None:
        now = datetime.datetime.now(datetime.timezone.utc)
        # get the next closest 8pm UTC+0 as this is the reset
        resettime = datetime.datetime(year=now.year, month=now.month, day = now.day, hour = 20, minute = 0, tzinfo=datetime.timezone.utc)
        if (resettime <= now):
            # add a day if past reset
            resettime += datetime.timedelta(days=1)
        
        secondsremaining = resettime - now
        message = "The Daily Reset is at 5AM JST. Time Remaining: " +convert_time(secondsremaining.total_seconds())
        await interaction.response.send_message(message,ephemeral=True)

    @app_commands.command(name="accountlink", description="Sends the message of how to account link")
    @app_commands.checks.cooldown(rate=1, per=1200)
    async def account_link(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("https://media.discordapp.net/attachments/413818124136087573/1091853105416638604/1518755127873.png?ex=65ece3f1&is=65da6ef1&hm=048e9942c2c21f479fb3bc191a0a9c55f48191ec3ee18f1dd0b1bf392821f1e8&=&format=webp&quality=lossless&width=810&height=241")



    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MainFAQ(bot))