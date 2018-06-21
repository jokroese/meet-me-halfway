# -*- coding: utf-8 -*-
#%% Initialise the program
import requests
import json

api_key = ''
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

<<<<<<< HEAD
def generateURL(basicurl,params):
    """Creates the working url we want"""
    for element in params:
        basicurl = basicurl + '/' + element
    basicurl = basicurl + '?apiKey=' + api_key
    return basicurl

def get_place_name_from_code(code):
    global placeZip
    for element in placeZip:
        if element[1] == code:
            return element[0]
    return False

def get_code_from_name(airportinfo,name):
    return airportinfo['AirportID'][airportinfo['Airport Name'].index(str(name))]

def get_name_from_code(airportinfo,name):
    return airportinfo['Airport Name'][airportinfo['AirportID'].index(str(name))]

def enterName(airportinfo):
    airport = input('Enter the airport you are planning to fly from... \n')
    try:
        get_code_from_name(airportinfo,airport)
        return get_code_from_name(airportinfo,airport)
    except:
        #if not a recognised name, suggest names which they may have meant
        print(airport+' is not a recognised place')
        if suggester(airport) is None:
            print('Did you mean....')
            suggester(airport[0:4])
        else: 
            print('Did you mean...')
            suggestions = suggester(airport)
            for i in suggestions:
                print(i)


=======
>>>>>>> parent of 4fcea60... Merge remote-tracking branch 'origin/master'
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

<<<<<<< Updated upstream
name = 'Andorrrb'
=======
name = 'New Zealand'
>>>>>>> Stashed changes
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
<<<<<<< HEAD
    placeZip = []
    for i in quotesJSON['Places']:
        placeZip.append([i['Name'],i['PlaceId']])
    return quotesDict, placeZip

#%%Generate all quotes for both origins
k = 1430 #Manchester
q = 1816    #Cape town
q = airportids.index('SFO') #san francisco international airport
q = airportids.index('DFW') #dallas fort worth

country = 'UK'
currency = 'GBP'
originPlace1 = airportids[k]
originPlace2 = airportids[q]
destinationPlace = "anywhere"
outboundPartialDate = "2017-11"
quotearray = []

params1 = [country, currency, locale, originPlace1, destinationPlace, outboundPartialDate]
params2 = [country, currency, locale, originPlace2, destinationPlace, outboundPartialDate]

qdict1,placeZip = quotesDict(generateURL(browseQuotesURL,params1))
qdict2,placeZip = quotesDict(generateURL(browseQuotesURL,params2))

#%%

def findMutual(qdict1,qdict2):
    """Find the mutual city based on two dictionaries"""
    destin1 = [i['DestinationId'] for i in qdict1]
    prices1 = [i['Price'] for i in qdict1]
    destin2 = [i['DestinationId'] for i in qdict2]
    prices2 = [i['Price'] for i in qdict2]
    mutualDest = list(set(destin1).intersection(destin2))
    
    mutualQuotes = []
    for i in mutualDest:
        index1 = destin1.index(i)
        index2 = destin2.index(i)
        templine = [destin1[index1], prices1[index1]+prices2[index2]]
        mutualQuotes.append(templine)
    
    prices = [i[1] for i in mutualQuotes]
    minPriceIndex = prices.index(min(prices))
    bestDest = get_place_name_from_code([i[0] for i in mutualQuotes][minPriceIndex])
<<<<<<< Updated upstream
    return bestDest
=======
    return quotesDict


>>>>>>> parent of 4fcea60... Merge remote-tracking branch 'origin/master'




=======
    return bestDest
>>>>>>> Stashed changes
