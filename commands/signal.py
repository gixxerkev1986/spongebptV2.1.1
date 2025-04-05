import discord
from discord.ext import commands
from utils.ta import generate_signal

class Signal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="signal", description="Genereer een koop/verkoop signaal.")
    async def signal(self, interaction: discord.Interaction, coin: str):
        await interaction.response.defer()
        signaal = generate_signal(coin)
        await interaction.followup.send(f"**{coin.upper()} – Signaal**\n{signaal}")
