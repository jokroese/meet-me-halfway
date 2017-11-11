# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:08:09 2017

@author: Sebastian
"""

import requests

api_key = 'ha177649362715475514428886582394'


#basicurl = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/'
locales = requests.get("http://partners.api.skyscanner.net/apiservices/reference/v1.0/locales?apiKey="+api_key)
markets = requests.get("http://partners.api.skyscanner.net/apiservices/reference/v1.0/markets?apiKey="+api_key)
currencies = requests.get("http://partners.api.skyscanner.net/apiservices/reference/v1.0/currencies?apiKey="+api_key)


autoSuggest = requests.get("http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/country?query={fran}&apiKey="+api_key)
country = 'AD' #or FR-sky?
locale = 'en-GB'
currency = 'USD'
browseDates = requests.get("http://partners.api.skyscanner.net/apiservices/browsedates/v1.0/\
                           {"+country+"}/{"+currency+"}/{"+locale+"}\
                           /{originPlace}/{destinationPlace}\
                           /{outboundPartialDate}/{inboundPartialDate}?apiKey="+api_key)


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