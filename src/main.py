from flask import Flask
app = Flask(__name__)

@app.route("/route/")
def hello():
    return "Hello World!"