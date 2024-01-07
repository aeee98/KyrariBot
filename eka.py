from discord import app_commands, Interaction
from discord.ext import commands
from dotenv import dotenv_values
from util import faq_dict


config = dotenv_values(".env")
eka_commands_usage_list = config.get("EKA_COMMANDS_LIST").split(",")
eka_commands_key_list = ["prifes", "coinshop", "gachaforecast", "gachaguide"]
eka_commands_choice_list = []
for key in eka_commands_key_list:
    eka_commands_choice_list.append(app_commands.Choice(name=key, value = key))

# Eka Cog is designed for population of specific data. These are designed specified for a specific list of people to be able to edit. This removes the need to include specific roles to redo the structure.
# This is named after Eka, one of the main contributors of the Princess Connect Discord server who creates most of the helpful forecasts and guides in the server.
class Eka(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # This is the main eka function. I don't really like slash commands for these types but to be dead honest I am lazy to parse values.
    @app_commands.command(name="ekaupdate", description="Updates the key list")
    @app_commands.rename(mode="key")
    @app_commands.describe(mode="type you want to modify")
    @app_commands.choices(mode = eka_commands_choice_list)
    async def update_db(self, interaction: Interaction, mode: app_commands.Choice[str], value : str) -> None:
        if interaction.user.id in eka_commands_usage_list:
            update_dict(mode.value, value)
            await interaction.response.send_message("Editing of key is successful.", ephemeral=True)
            # Probably want to send a log message to a master channel but for now I will leave it as is.
        else:
            await interaction.response.send_message("You are not allowed to use this function.", ephemeral=True)



    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")
    
    
def update_dict(key : str, value: str) -> None:
        faq_dict[key] = value

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Eka(bot))