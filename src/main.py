#--- Initialise the program
# Flask side
from flask import Flask, jsonify, render_template, request
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

#--- Basic setup of jQuery
<script type=text/javascript>
  $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
</script>

#--- Suggest place names when half-typed
@app.route('/me')
def suggester(query):
    """Returns suggestions if the input is incorrect"""
    #query = 'fran'
    autoSuggest = requests.get(refurl+"autosuggest/v1.0/RU/USD/en-GB?query="+query+"&apiKey="+api_key)
    autoSuggJSON = json.loads(autoSuggest.text)
    return [i['PlaceName'] for i in autoSuggJSON['Places']]


@app.route("/hello/<username>")
def hello_user(username):
    return "Hello {}!".format(username)

#--- When form is submitted, run algorithm to find cheapest flight and bring to new page
@app.route('/showResults/')
def showResults():
    return render_template('results.html')




#--- Make sure this comes last
if __name__ == "__main__":
    app.run()