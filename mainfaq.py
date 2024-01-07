import discord
from discord import app_commands
from discord.ext import commands
from dotenv import dotenv_values
from util import faq_dict

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
    async def gacha_forecast(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(faq_dict["gachaforecast"], ephemeral = True)

    @app_commands.command(name="gachaguide", description="Sends you the link to the gacha guide by Eka. This message is private.")
    async def gacha_forecast(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(faq_dict["gachaguide"], ephemeral = True)

    @app_commands.command(name="prifes", description="Shows the priority list for all Prifes Banners by Kyrari. This message is private.")
    async def prifes_guide(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(faq_dict["prifes"], ephemeral = True)

    @app_commands.command(name="coinshop", description="Shows the priority list for all the currency shops by Wazahai. This message is private.")
    async def coinshop_guide(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(faq_dict["coinshop"], ephemeral = True)


    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MainFAQ(bot))