import discord
from discord import app_commands
from discord.ext import commands
from dotenv import dotenv_values

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
        await interaction.response.send_message("https://media.discordapp.net/attachments/413818124136087573/1192460199538204762/A.png?ex=65a9281a&is=6596b31a&hm=d57c6b2fb045239fa1e76b9a8b2556fe338de0f3fefe5ebfeacab61c68ca7569&=&format=webp&quality=lossless&width=810&height=818", ephemeral = True)

    @app_commands.command(name="gachaguide", description="Sends you the link to the gacha guide by Eka. This message is private.")
    async def gacha_forecast(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("https://media.discordapp.net/attachments/413818124136087573/1192461474363355176/Winter_2023-24_Gacha_Banner_Guide_EN.png?ex=65a9294a&is=6596b44a&hm=e1de925d55268d9f21bf956e2883b27b3e1417dddba2076ce0b4297afdf72cd6&=&format=webp&quality=lossless&width=810&height=550", ephemeral = True)

    @app_commands.command(name="prifes", description="Shows the priority list for all Prifes Banners by Kyrari. This message is private.")
    async def prifes_guide(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/413818124136087573/1191612708412477570/image.png?ex=65a612d0&is=65939dd0&hm=4dce5d78a6d13340d3c0a1a6dda8f8cfc7adb1ee028520decc6f9fd32843a0fb&", ephemeral = True)

    @app_commands.command(name="coinshop", description="Shows the priority list for all the currency shops by Wazahai. This message is private.")
    async def coinshop_guide(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1091424363875672064/1163194170178015242/coin_shop_prio_oct2023.png", ephemeral = True)


    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")



async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(MainFAQ(bot))