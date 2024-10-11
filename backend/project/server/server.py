from flask import Flask
from flask import request, make_response, jsonify
import traceback

from vision import get_coords

app = Flask(__name__)


# A POST request is used whenever we change the server's state
# Here we're donwloading a file
@app.route('/odlc', methods=["POST"])
def process_image():

    ### YOUR CODE HERE ###

        # get the image data
        
        # call get_coords, passing in the image bytes

    # if an exception occurred, print the exception return 400

    # return the coords in a json response

    pass  # DELETE THIS