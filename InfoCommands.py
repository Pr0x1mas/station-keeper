import json
from urllib.request import Request, urlopen
from discord.ext import commands
import keyFinder
import pprint
import InfoDataValues as IDV

class InfoCommands(commands.Cog):
    '''Commands for getting info about an object'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="shows raw info about a station", description="shows raw info about a station or carrier", aliases=['carrier'])
    async def station(self, ctx, name):
        async with ctx.typing():
            try:
                stationname = name.replace(" ", "%20") # convert spaces to %20 for url

                url = 'https://eddbapi.kodeblox.com/api/v4/stations?name=' + stationname # get data for station
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                raw_station = urlopen(req).read()
                station = json.loads(raw_station)["docs"] # parse station data as json
                pruned_station = []

                pruned_station_data = keyFinder.findKeys("station", name, IDV.station, "name") # get key values for the keys specified in InfoDataValues.py
                
                pruned_station_data['system_id'] = keyFinder.findKey('system', str(pruned_station_data['system_id']), 'name', 'eddbid') # convert system ID value to name
                
                formatted_pruned_station_data = []
                
                for key, value in pruned_station_data.items():
                    formatted_pruned_station_data.append(str(key).replace('id', 'name').replace('_', ' ').capitalize() + ': ' + str(value).capitalize()) # make dictionary look kinda nice and change system id to system name

                await ctx.send("**" + name.upper() + "** \n \n" + '\n'.join(formatted_pruned_station_data))
            
            except Exception as E:
                if str(E) == 'list index out of range':
                    await ctx.send("Station '" + name + "' does not exist.")
                    
                else:
                    await ctx.send(str(E) + "\n \n Please contact @Pr0x1mas#0632 if this error persists")
                    
                    
                    
    @commands.command(brief="shows raw info about a system", description="shows raw info about a system")
    async def system(self, ctx, name):
        async with ctx.typing():
            try:
                systemname = name.replace(" ", "%20") # convert spaces to %20 for url

                url = 'https://eddbapi.kodeblox.com/api/v4/systems?name=' + systemname # get data for system
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                raw_system = urlopen(req).read()
                system = json.loads(raw_system)["docs"] # parse system data as json
                pruned_system = []

                pruned_system_data = keyFinder.findKeys("system", name, IDV.system, "name") # get key values for the keys specified in InfoDataValues.py
                
                formatted_pruned_system_data = []
                
                for key, value in pruned_system_data.items():
                    formatted_pruned_system_data.append(str(key).replace('_', ' ').capitalize + ': ' + str(value).capitalize()) # make dictionary look kinda nice

                await ctx.send("**" + name.upper() + "** \n \n" + '\n'.join(formatted_pruned_system_data))
            
            except Exception as E:
                if str(E) == 'list index out of range':
                    await ctx.send("system '" + name + "' does not exist.")
                    
                else:
                    await ctx.send(str(E) + "\n \n Please contact @Pr0x1mas#0632 if this error persists")


def setup(bot):
    bot.add_cog(InfoCommands(bot))
