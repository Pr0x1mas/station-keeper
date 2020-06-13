import json
from urllib.request import Request, urlopen
from discord.ext import commands

class EDDBCommands(commands.Cog):
    '''Commands that use the EDDB API'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='finds a station or fleet carrier', description="Finds a station or fleet carrier. With fleet carriers, you must use its identification code in the format 'xxx-xxx'. If a station name has a space in it, enclose the name in quotation marks.")
    async def findCarrier(self, ctx, station):
        async with ctx.typing():
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

                await ctx.send(":satellite_orbital: Carrier/station " + carriername + " is at system " + systemname) # send message showing whereabouts of station

            except Exception:
                await ctx.send(":satellite_orbital: Carrier/station " + carriername + " could not be found. Bear in mind that carriers must be identified by their code, in the format 'XXX-XXX'") # if there are any errors, show this message

def setup(bot):
    bot.add_cog(EDDBCommands(bot))