# -*- coding: utf-8 -*-
#%% Initialise the program
import requests
import json

api_key = 'ha177649362715475514428886582394'
refurl = "http://partners.api.skyscanner.net/apiservices/"

#%%Define some functions
def convertCountry(zippedList,name):
    """Converts a country name to the corresponding country code"""
    #e.g. Russia --> RU
    codeIndex = [i[1] for i in zippedList].index(name)
    print(zippedList[codeIndex][0])
    return zippedList[codeIndex][0]

def suggester(query):
    """Returns suggestions if the input is incorrect"""
    #query = 'fran'
    autoSuggest = requests.get(refurl+"autosuggest/v1.0/RU/USD/en-GB?query="+query+"&apiKey="+api_key)
    autoSuggJSON = json.loads(autoSuggest.text)
    return [i['PlaceName'] for i in autoSuggJSON['Places']]

#%% Get info on locales
locdata = {'Code':"codeval","Name":"nameval"}
localesreq = requests.get(refurl + "reference/v1.0/locales?apiKey=" + api_key, data= locdata)
localesreq = json.loads(localesreq.text)
localecodes = []
localenames = []
i=0
while i<len(localesreq['Locales']):
    localenames.append(localesreq["Locales"][i]["Name"])
    localecodes.append(localesreq['Locales'][i]["Code"])
    i+=1
locale = localecodes[12]

currency = 'USD'
currencies = requests.get(refurl+"reference/v1.0/currencies?apiKey="+api_key)

#%%Get info  on markets
markets = requests.get(refurl + "reference/v1.0/countries/" + locale + "?apiKey=" + api_key)
markets = json.loads(markets.text)

marketcodes = []
marketnames = []
i=0
while i<len(markets['Countries']):
    marketnames.append(markets["Countries"][i]["Name"])
    marketcodes.append(markets['Countries'][i]["Code"])
    i+=1
del i;

countriesZip = list(zip(marketcodes,marketnames))
countriesdict = {"Codes":marketcodes,
                "Names":marketnames
                }

name = 'Andorrrb'
"""Convert the country to a code which we can use"""
try:
    convertCountry(countriesZip,name)
except:
    #if not a recognised name, suggest names which they may have meant
    print(name+' is not a recognised place')
    if suggester(name) is None:
        print('Did you mean....')
        suggester(name[0:4])
    else: 
        print('Did you mean...')
        suggester(name)

#%%Browse routes basic
country = 'RU'
locale = 'en-GB'
currency = 'USD'
originPlace = 'RU'
destinationPlace = 'UK'
outboundPartialDate = '2017-11-22'
inboundPartialDate = ''

#%%Faulty
#def browseDict(country,locale,currency,originPlace,destinationPlace,outboundPartialDate,inboundPartialDate):
#    """Generates a usable list of routes from an input"""
#    browseRoutes = requests.get(refurl+"/browseroutes/v1.0/"+country+"/"+currency+"/"+locale+"/"+originPlace+"/"+destinationPlace+"/"+outboundPartialDate+"/?apiKey="+api_key)
#    routesJSON = json.loads(browseRoutes.text)
#    browseDict = []
#    for i in routesJSON['Routes']:
#        smallDict = {'DestinationId':i['DestinationId'],
#                     'OriginId':i['OriginId'],
#                     'Price':i['Price']}
#        browseDict.append(smallDict)
#        print(i['OriginId'],i['DestinationId'])
#    return browseDict

#%% Browse quotes basic
def quotesDict(country,locale,currency,originPlace,destinationPlace,outboundPartialDate,inboundPartialDate):
    """Generates a usable list of quotes from an input"""
    browseQuotes = requests.get(refurl+"browsequotes/v1.0/"+country+"/"+currency+"/"+locale+"/"+originPlace+"/"+destinationPlace+"/"+outboundPartialDate+"/"+inboundPartialDate+"?apiKey="+api_key)
    quotesJSON = json.loads(browseQuotes.text)
    quotesDict = []
    for i in quotesJSON['Quotes']:
        print(i)
        i = i
        smallDict = {'Price':i['MinPrice'],
                     'OriginId':i['OutboundLeg']['OriginId'],
                      'DepartureDate':i['OutboundLeg']['DepartureDate'],
                      'DestinationId':i['OutboundLeg']['DestinationId']}
        quotesDict.append(smallDict)
    return quotesDict






