import json
from urllib.request import Request, urlopen
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path = os.path.join(os.path.dirname(__file__), '.env'))
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    
@bot.command()
async def findCarrier(ctx, station):
    try:
        carriername = station.replace(" ", "%20") # convert spaces to %20 for url

        url = 'https://eddbapi.kodeblox.com/api/v4/stations?name=' + carriername # get data for station
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        raw_station = urlopen(req).read()

        station = json.loads(raw_station) # parse station data as json and get system id
        systemid = station.get("docs")[0].get("system_id")

        url = 'https://eddbapi.kodeblox.com/api/v4/systems?eddbid=' + str(systemid) # get data for system
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        raw_system = urlopen(req).read()

        system = json.loads(raw_system) # parse system data as json and get system name
        systemname = system.get("docs")[0].get("name")

        print("Carrier/station " + carriername + " is at system " + systemname)

        await ctx.send("Carrier/station " + carriername + " is at system " + systemname)
    
    except Exception:
        await ctx.send("Carrier/station " + carriername + " could not be found")

if __name__ == "__main__":
    bot.run(TOKEN)
