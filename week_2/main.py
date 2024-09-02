from flask import Flask
from flask import request, make_response
import web_scraper

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# A POST request is used whenever we change the server's state
# Here we're donwloading a file
@app.route('/scrape', methods=["POST"])                         # accept HTTP POST requests at /scrape
def scrape():                                                   # when a POST request is received on /scrape, run this function
    try:
        url = request.form.get('url')                           # get url parameter
        web_scraper.download(url)                               # download the webpage

    except Exception as e:
        return make_response("Invalid URL. " + str(e), 400)     # HTTP 400 = Bad Request

    return make_response("Website download successful", 200)    # HTTP 200 = Success
