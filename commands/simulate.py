import discord
from discord.ext import commands

class Simulate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="simulate", description="Simuleer een trade/backtest van een coin.")
    async def simulate(self, interaction: discord.Interaction, coin: str, buy_price: float, sell_price: float):
        result = (sell_price - buy_price) / buy_price * 100
        await interaction.response.send_message(f"Simulatie voor {coin.upper()}: winst/verlies = {result:.2f}%")
