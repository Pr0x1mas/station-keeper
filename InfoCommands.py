import json
from urllib.request import Request, urlopen
from discord.ext import commands

class InfoCommands(commands.Cog):
    '''Commands for getting info about an object'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="shows raw info about a system", description="shows raw info about a system")
    async def system(self, ctx, name):
        async with ctx.typing():
            try:
                systemname = name.replace(" ", "%20") # convert spaces to %20 for url

                url = 'https://eddbapi.kodeblox.com/api/v4/systems?name=' + systemname # get data for system
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                raw_system = urlopen(req).read()
                system = json.loads(raw_system)["docs"] # parse system data as json
                await ctx.send("```" + json.dumps(system, indent=4, sort_keys=True) + "```")
            except Exception:
                await ctx.send("unable to get system data")

    @commands.command(brief="shows raw info about a station", description="shows raw info about a station")
    async def station(self, ctx, name):
        async with ctx.typing():
            try:
                stationname = name.replace(" ", "%20") # convert spaces to %20 for url

                url = 'https://eddbapi.kodeblox.com/api/v4/stations?name=' + stationname # get data for station
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                raw_station = urlopen(req).read()
                station = json.loads(raw_station)["docs"] # parse station data as json
                await ctx.send("```" + json.dumps(station, indent=4, sort_keys=True) + "```")
            except Exception:
                await ctx.send("unable to get station data")

def setup(bot):
    bot.add_cog(InfoCommands(bot))
