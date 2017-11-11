# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:08:09 2017

@author: Sebastian
"""

import requests

api_key = 'ha177649362715475514428886582394'


#basicurl = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/'
refurl = "http://partners.api.skyscanner.net/apiservices/"
locales = requests.get(refurl+"reference/v1.0/locales?apiKey="+api_key)
markets = requests.get(refurl+"reference/v1.0/countries/en-GB?apiKey="+api_key)
currencies = requests.get(refurl+"reference/v1.0/currencies?apiKey="+api_key)


autoSuggest = requests.get(refurl+"autosuggest/v1.0/RU/USD/en-GB?query={fran}&apiKey="+api_key)
country = 'RU'
locale = 'en-GB'
currency = 'USD'
originPlace = 'RU'
destinationPlace = 'PT'
outboundPartialDate = '2017-11'
inboundPartialDate = '2017-11-10'

browseRoutes = requests.get(refurl+"/browseroutes/v1.0/"+country+"/"+currency+"/"+locale+"/"+originPlace+"/"+destinationPlace+"/"+outboundPartialDate+"/?apiKey="+api_key)

#browseQuotes = requests.get(refurl+"browsequotes/v1.0/\
#                           {"+country+"}/{"+currency+"}/{"+locale+"}\
#                           /{originPlace}/{destinationPlace}/\
#                           {outboundPartialDate}/{inboundPartialDate}?apiKey="+api_key)



#originPlaces = 
#destinationPlaces = 
#inboundPartialDates = 
#params = [country, currency, locale, originPlace, destinationPlace, inboundPartialDate]
#requrl=basicurl
#for element in params:
#    requrl = requrl + '/' + element
#requrl = requrl + '?apiKey=' + api_key
#browsequotes =  requests.get(requrl, headers=headers, params=params)

#print(currencies.text)