import discord
from discord.ext import commands
import json

class SetFee(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="setfee", description="Stel de trade fee in voor je exchange.")
    async def setfee(self, interaction: discord.Interaction, fee: float):
        user_id = str(interaction.user.id)
        with open("user_settings.json", "r+") as f:
            data = json.load(f)
            if user_id not in data:
                data[user_id] = {}
            data[user_id]["fee"] = fee
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
        await interaction.response.send_message(f"Fee ingesteld op: {fee}%")
