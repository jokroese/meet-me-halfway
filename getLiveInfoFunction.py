import requests
import json

exampleLiveParams = ["Economy","UK","GBP","en-GB","iata",'MAN','MXP','2017-11-13',"",1,0,0]

def getLiveInfo(liveParams):
    api_key = 'ha177649362715475514428886582394'
    ip = requests.get('https://api.ipify.org')
    ip = ip.text
    """
    cabinclass, country, currency, locale, locationSchema, originplace, destinationplace, 
    outbounddate, inbounddate, adults, children, infants, apikey = liveParams
    """
    
    """
    Create live session to find our cheapest flights
    
    Input above parameters; return an url of our search results for these parameters
    
    """

    headers = {'Content-Type': 'application/x-www-form-urlencoded',
        'X-Forwarded-For':ip
    }

    data = {
      'cabinclass':liveParams[0],
      'country':liveParams[1],
      'currency':liveParams[2],
      'locale':liveParams[3],
      'locationSchema':liveParams[4],
      'originplace':liveParams[5],
      'destinationplace':liveParams[6],
      'outbounddate':liveParams[7],
      'inbounddate':liveParams[8],
      'adults':liveParams[9],
      'children':liveParams[10],
      'infants':liveParams[11],
      'apikey':api_key,
    }
    locationUrl = requests.post('http://partners.api.skyscanner.net/apiservices/pricing/v1.0', headers=headers, data=data)
    print(locationUrl.headers["Location"])
    """
    Take our parameters and find the list of journey times, prices and links to
    relevant booking details.
    
    """
    searchResults = requests.get(locationUrl.headers['Location'] + "?apiKey="+ api_key)
    searchResults = json.loads(searchResults.text)
    departureTimes = [element["Departure"] for element in searchResults['Legs']]
    arrivalTimes = [element["Arrival"] for element in searchResults['Legs']]
    pricingOptions = [element["PricingOptions"] for element in searchResults["Itineraries"]]
    prices = [i[0]["Price"] for i in pricingOptions]
    deepLinks = [i[0]["DeeplinkUrl"] for i in pricingOptions]
    liveInfo = []
    for i in range(len(departureTimes)):
        templine = [departureTimes[i],arrivalTimes[i],prices[i],deepLinks[i]]
        liveInfo.append(templine)
		
    return liveInfo