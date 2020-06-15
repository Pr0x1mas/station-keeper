# this script fetches a key value from an eddb record. It should not be used for multiple keys from the same record as this is inneficient and will keep reloading a record it does not need to

import json
from urllib.request import Request, urlopen

def findKey(mode, term, key, mode2): #mode is for whether it is a station or a system etc. Mode2 is whether you are searching by the name or eddbid etc.
    
    # get data from API depending on what you are looking for
    if mode == "station":
        url = 'https://eddbapi.kodeblox.com/api/v4/stations?' + mode2 + '=' + str(term)
    elif mode == "system":
        url = 'https://eddbapi.kodeblox.com/api/v4/systems?' + mode2 + '=' + term
    elif mode == "body":
        url = 'https://eddbapi.kodeblox.com/api/v4/bodies?' + mode2 + '=' + term
    elif mode == "faction":
        url = 'https://eddbapi.kodeblox.com/api/v4/factions?' + mode2 + '=' + term
    
    
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    raw_data = urlopen(req).read()

    data = json.loads(raw_data) # parse station data as json and get system id
    found_key = data.get("docs")[0].get(key)
    
    return found_key


def findKeys(mode, term, keys, mode2): #same as other function but takes keys as a list and returns all of them in a dictionary


    # get data from API depending on what you are looking for
    if mode == "station":
        url = 'https://eddbapi.kodeblox.com/api/v4/stations?' + mode2 + '=' + term.replace(" ", "%20") # convert spaces to %20 for url
    elif mode == "system":
        url = 'https://eddbapi.kodeblox.com/api/v4/systems?' + mode2 + '=' + term.replace(" ", "%20") # convert spaces to %20 for url
    elif mode == "body":
        url = 'https://eddbapi.kodeblox.com/api/v4/bodies?' + mode2 + '=' + term.replace(" ", "%20") # convert spaces to %20 for url
    elif mode == "faction":
        url = 'https://eddbapi.kodeblox.com/api/v4/factions?' + mode2 + '=' + term.replace(" ", "%20") # convert spaces to %20 for url
    
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    raw_data = urlopen(req).read()

    data = json.loads(raw_data) # parse station data as json and get system id

    found_keys = {}

    for i in range(len(keys)):
        found_keys[keys[i]] = found_key = data.get("docs")[0].get(keys[i])
        
    return found_keys
