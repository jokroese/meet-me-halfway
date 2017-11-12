#import scrBrowseRoutestidied
browseQuotesURL = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0'
api_key = 'ha177649362715475514428886582394'
#airportDatabasePathway = "C:/Users/georg/Documents/GitHub/meet-me-halfway/airports.csv"
exampleInput = "me=Manchester&you=Cape+Town&departure=11%2F13%2F2017&return=11%2F28%2F2017&trip=single"
def inputToParams(onlineInput):
	#onlineInput ="me=Manchester&you=Cape+Town&departure=11%2F13%2F2017&return=11%2F28%2F2017&trip=round"
	inputParams=onlineInput.split("&")
	inputParams = [i[i.index("=")+1:].replace("+"," ") for i in inputParams]
	#print(inputParams)
	inputParams[2] = inputParams[2][-4:] + "-" + inputParams[2][:2] + "-"  + inputParams[2][5:7]
	inputParams[3] = inputParams[3][-4:] + "-" + inputParams[3][:2] + "-"  + inputParams[3][5:7]
	if inputParams[4] == 'round':
		inputParams[4] = True
	else:
		inputParams[4] = False
		
	# with open(airportDatabasePathway,"r",encoding="utf8") as input_file:
		# airportAllInfo = []
		# for line in input_file:
			# newLine = [x.strip().replace('"','') for x in line.split(',')]
			# newLine = newLine[1:5]
			# airportAllInfo.append(newLine)
		# for thing in airportAllInfo:
			# if thing[0][-8:] != " Airport":
				# thing[0] = thing[0] + " Airport"
			
	# """
	# airportAllInfo returns list of lists with elements:
	# [ Airport Name , City , Country , IATA code ]
	
	# """
	# anames = set([i[0] for i in airportAllInfo])
	# acities = set(i[1] for i in airportAllInfo])
	# acountries = set([i[2] for i in airportAllInfo])
	
	# if inputParams[0] is in anames:
		# index1 = [i[0] for i in airportAllInfo].index(inputParams[0])
	# elif inputParams[0] is in acities:
		# index1 = [i[1] for i in airportAllInfo].index(inputParams[0])
	# elif inputParams
	
	# try:
		# index1 = [i[0] for i in airportAllInfo].index(inputParams[0])
		# index2 = [i[0] for i in airportAllInfo].index(inputParams[1])
	# except:
		# index1 = [i[0][:-8] for i in airportAllInfo].index(inputParams[0])
		# index2 = [i[0][:-8] for i in airportAllInfo].index(inputParams[1])
		
	# inputParams[0] = airportAllInfo[index1][3]
	# inputParams[1] = airportAllInfo[index2][3]
	# """
	# Will return an array of the form
	# [ Place 1 , Place 2 , Departure Date , Return Date  (all string) , RoundTrip (boolean) ] 
	
	# """
	return inputParams
	
print(inputToParams(exampleInput))