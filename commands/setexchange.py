import discord
from discord.ext import commands
import json

class SetExchange(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="setexchange", description="Kies je exchange (bijv. binance, kucoin, etc.)")
    async def setexchange(self, interaction: discord.Interaction, exchange: str):
        user_id = str(interaction.user.id)
        with open("user_settings.json", "r+") as f:
            data = json.load(f)
            if user_id not in data:
                data[user_id] = {}
            data[user_id]["exchange"] = exchange
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
        await interaction.response.send_message(f"Exchange ingesteld op: {exchange}")
