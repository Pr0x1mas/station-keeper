import json
from urllib.request import Request, urlopen
from discord.ext import commands
import keyFinder

class MiscCommands(commands.Cog):
    '''Miscellaneous Commands'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='finds a station or fleet carrier', description="Finds a station or fleet carrier. With fleet carriers, you must use its identification code in the format 'xxx-xxx'. If a station name has a space in it, enclose the name in quotation marks.")
    async def findCarrier(self, ctx, station):
        async with ctx.typing():
            try:
                system_id = keyFinder.findKey("station", station, "system_id", "name") # get ID of system station is in
                system_name = keyFinder.findKey("system", str(system_id), "name", "eddbid") # use ID to get system name

                await ctx.send(":satellite_orbital: Carrier/station " + station + " is at system " + system_name) # send message showing whereabouts of station

            except Exception as E:
                await ctx.send(":satellite_orbital: Carrier/station " + station + " could not be found. Bear in mind that carriers must be identified by their code, in the format 'XXX-XXX'. \n \n Reason: " + str(E)) # if there are any errors, show this message along with said error

def setup(bot):
    bot.add_cog(MiscCommands(bot))