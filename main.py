import os
from discord.ext import commands
import discord

try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path = os.path.join(os.path.dirname(__file__), '.env'))
except Exception:
    print("Unable to load dotenv, reverting to system environment variable")
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix='?', description='A Discord bot by Pr0x1mas that uses the EDDB API. See https://Pr0x1mas.github.io/station-keeper for more information.')

bot.load_extension("MiscCommands")
bot.load_extension("InfoCommands")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="EDDB.io"))

bot.run(TOKEN)

