# Meet Me Halfway - API Parsing
#
# Import some functions and libraries
import requests
import pandas as pd
import json
from pprint import pprint

# Define our API key and urls
api_key= "ha177649362715475514428886582394"
refurl = "http://partners.api.skyscanner.net/apiservices/reference/v1.0/"
basicurl = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/'

# Extract all locales from skyscanner API 
locdata = {'Code':"codeval","Name":"nameval"}
localesreq = requests.get(refurl + "locales?apiKey=" + api_key, data= locdata)
localesreq = json.loads(localesreq.text)

localecodes = []
localenames = []
i=0
while i<len(localesreq['Locales']):
    localenames.append(localesreq["Locales"][i]["Name"])
    localecodes.append(localesreq['Locales'][i]["Code"])
    i+=1
	
localeszip = zip(localecodes, localenames)
# All locales now saved in these two arrays, codes and names	


# Extract all currencies from skyscanner API
currencies = requests.get(refurl + "currencies?apiKey=" +api_key)
currencies = json.loads(currencies.text)

currcodes = []
currsymbols = []
currthousep = []
currdecsep = []
currsymleft = []
currspace = []
currroundcoeff = []
currdecdigits = []
i=0
while i<len(currencies["Currencies"]):
    currcodes.append(currencies["Currencies"][i]["Code"])
    currsymbols.append(currencies["Currencies"][i]["Symbol"])
    currthousep.append(currencies["Currencies"][i]["ThousandsSeparator"])
    currdecsep.append(currencies["Currencies"][i]["DecimalSeparator"])
    currsymleft.append(currencies["Currencies"][i]["SymbolOnLeft"])
    currspace.append(currencies["Currencies"][i]["SpaceBetweenAmountAndSymbol"])
    currroundcoeff.append(currencies["Currencies"][i]["RoundingCoefficient"])
    currdecdigits.append(currencies["Currencies"][i]["DecimalDigits"])
    i+=1
#print(currcodes)


# Extract all markets from skyscanner API
# (this contains countries and country codes
marketnames = []
i=0
while i<len(markets['Countries']):
    marketnames.append(markets["Countries"][i]["Name"])
    marketcodes.append(markets['Countries'][i]["Code"])
    i+=1
print(marketcodes)
countrieszip = zip(marketcodes,marketnames)
countriesdict = {"Codes":marketcodes,
                "Names":marketnames
                }
				
				
# Extract all places from skyscanner API
# (contains all countries, cities & airports)
places = requests.get("http://partners.api.skyscanner.net/apiservices/geo/v1.0?apiKey="+api_key)
places = json.loads(places.text)

#print(places)