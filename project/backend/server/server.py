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

    try:
        # get the image data
        img_data = request.get_json()
        img_num = img_data['img_name']
            
        # call get_coords, passing in the image bytes
        x_dist, y_dist = get_coords(img_num)

        response_json = {
            'x_dist': x_dist,
            'y_dist': y_dist
        }

    except Exception as e:
        # if an exception occurred, print the exception return 400
        response_json = {
            'x_dist': -1,
            'y_dist': -1
        }
        
        print("Warning - Exception Occurred: ", e)
        return 400

    # return the coords in a json response
    return jsonify(response_json)