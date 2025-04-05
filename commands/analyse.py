import discord
from discord.ext import commands
from discord import app_commands
from utils.ta import analyse_multiple_timeframes

class Analyse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="analyse", description="Technische analyse voor meerdere timeframes")
    @app_commands.describe(coin="Bijv. kaspa, fet, link")
    async def analyse(self, interaction: discord.Interaction, coin: str):
        await interaction.response.defer()
        symbol = f"{coin.lower()}usdt"
        try:
            resultaten = analyse_multiple_timeframes(symbol)

            if not resultaten:
                await interaction.followup.send(f"Geen TA-gegevens beschikbaar voor {symbol.upper()}")
                return

            embed = discord.Embed(
                title=f"Analyse voor {coin.upper()}",
                color=0x3498db
            )
            for tf, data in resultaten.items():
                embed.add_field(
                    name=f"{tf} timeframe",
                    value=f"RSI: {data['rsi']:.2f}\nEMA-trend: {data['trend']}\nPrijs: {data['close']:.5f}",
                    inline=False
                )

            await interaction.followup.send(embed=embed)
        except Exception as e:
            await interaction.followup.send(f"Fout bij ophalen analyse voor {symbol.upper()}: {str(e)}")

async def setup(bot):
    await bot.add_cog(Analyse(bot))