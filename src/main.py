#--- Initialise the program
# Flask side
from flask import Flask, render_template
app = Flask(__name__)

#Backend
import requests
import json

api_key = 'ha177649362715475514428886582394'
refurl = "http://partners.api.skyscanner.net/apiservices/"

#--- Basic setup of html
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

#--- Suggest place names when half-typed
@app.route('/suggester')
def suggester(query):
    """Returns suggestions if the input is incorrect"""
    #query = 'fran'
    autoSuggest = requests.get(refurl+"autosuggest/v1.0/RU/USD/en-GB?query="+query+"&apiKey="+api_key)
    autoSuggJSON = json.loads(autoSuggest.text)
    return [i['PlaceName'] for i in autoSuggJSON['Places']]