import discord
from discord.ext import commands
from utils.ta import analyse_coin
from utils.helpers import get_price

class Dagelijks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="dagelijks", description="Toon een dagelijkse analyse van een coin.")
    async def dagelijks(self, interaction: discord.Interaction, coin: str):
        await interaction.response.defer()
        prijs = get_price(coin)
        analyse = analyse_coin(coin)
        await interaction.followup.send(f"**{coin.upper()} – Dagelijkse Analyse**\nPrijs: {prijs} USD\nAnalyse: {analyse}")
