import requests
import json

def search_routes(originCode1,originCode2,date,details):
    api_key = 'ha177649362715475514428886582394'
    refurl = "http://partners.api.skyscanner.net/apiservices/"
    browseQuotesURL = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0'
    locales, currencies, markets,countriesZip,airportinfo = get_skyscanner_data(api_key,refurl,browseQuotesURL)
    # country, currency
    # quotes1 = browse_quotes(airportinfo,k,"Anywhere",markets,date,request_parameters,browseQuotesURL,api_key )
    # quotes2 = browse_quotes(airportinfo,k,"Anywhere",markets,date,request_parameters,browseQuotesURL,api_key )
    params1 = [details[0],details[1],details[2], originCode1, "Anywhere", date]
    params2 = [details[0],details[1],details[2], originCode2, "Anywhere", date]
    qdict1,placeZip = quotesDict(generateURL(browseQuotesURL,params1,api_key))
    qdict2,placeZip = quotesDict(generateURL(browseQuotesURL,params2,api_key))
    best_dest = findMutual(qdict1,qdict2,placeZip)
    return best_dest
   

   
def get_skyscanner_data(api_key,refurl,browseQuotesURL):
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
    locale = 'en-GB'

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
    places = requests.get(refurl+"/geo/v1.0?apiKey="+api_key)
    places = json.loads(places.text)
    airportids = []
    airportlocs = []
    airportnames = []
    airportcities = []
    airportcountries = []

    for continent in places["Continents"]:
        for country in continent["Countries"]:
            for city in country["Cities"]:
                for airport in city["Airports"]:
                    airportids.append(airport["Id"])
                    airportlocs.append(airport["Location"])
                    airportnames.append(airport["Name"])
                    airportcities.append(city["Name"])
                    airportcountries.append(city["CountryId"])               
    airportinfo = {"AirportID":airportids,
                   "Airport Location":airportlocs,
                   "Airport Name":airportnames,
                   "Airport City":airportcities,
                   "Airport Country":airportcountries
                  }
    return localesreq, currencies, markets,countriesZip,airportinfo

def generateURL(basicurl,params,api_key):

    """Creates the working url we want"""
    for element in params:
        basicurl = basicurl + '/' + element
    basicurl = basicurl + '?apiKey=' + api_key
    return basicurl

def browse_quotes(airportinfo,k,q,markets,date,request_info,browseQuotesURL,api_key):
    marketcodes = []
    marketnames = []
    i=0
    while i<len(markets['Countries']):
        marketnames.append(markets["Countries"][i]["Name"])
        marketcodes.append(markets['Countries'][i]["Code"])
        i+=1
    del i;
    
    country = request_info[0]
    currency = request_info[1]
    locale = request_info[2]
    originPlace = airportinfo["AirportID"][k]
    destinationPlace = "anywhere"   #airportids[q]
    print("Going from "+ airportinfo["Airport Name"][k] + " in " + 
          marketnames[marketcodes.index(airportinfo["Airport Country"][k])]
          + " to " + airportinfo["Airport Name"][q] + " in " + 
          marketnames[marketcodes.index(airportinfo["Airport Country"][q])])
    outboundPartialDate = date
    params = [country, currency, locale, originPlace, destinationPlace, outboundPartialDate]
    browsequotes =  requests.get(generateURL(browseQuotesURL,params,api_key))
    browsequotes = json.loads(browsequotes.text)
    print(browsequotes)

    
def get_place_name_from_code(code,placeZip):
    for element in placeZip:
        if element[1] == code:
            return element[0]
    return False
    
def findMutual(qdict1,qdict2,placeZip):
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
    bestDest = get_place_name_from_code([i[0] for i in mutualQuotes][minPriceIndex],placeZip)
    return bestDest

def quotesDict(browseQuotesURL):
    browsingurl = browseQuotesURL
    """Generates a usable list of quotes from an input"""
    browseQuotes = requests.get(browsingurl)
    quotesJSON = json.loads(browseQuotes.text)
    quotesDict = []
    for i in quotesJSON['Quotes']:
        #print(i)
        i = i
        smallDict = {'Price':i['MinPrice'],
                     'OriginId':i['OutboundLeg']['OriginId'],
                      'DepartureDate':i['OutboundLeg']['DepartureDate'],
                      'DestinationId':i['OutboundLeg']['DestinationId']}
        quotesDict.append(smallDict)
    placeZip = []
    for i in quotesJSON['Places']:
        placeZip.append([i['Name'],i['PlaceId']])
    return quotesDict, placeZip
    
k = "MAN" #Manchester
q = "CPT"  # Second Origin Index
date = "2017-11-12"
details = ["UK","GBP","en-GB","Anywhere"] # country, currency, locale,destinationPlace
best_dest= search_routes(k,q,date,details)