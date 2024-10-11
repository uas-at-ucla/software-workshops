from flask import Flask
from flask import request, make_response, jsonify
import traceback

from download import download

app = Flask(__name__)


# A POST request is used whenever we change the server's state
# Here we're donwloading a file
@app.route('/upload', methods=["POST"])
def upload():
    try:
        request_json = request.get_json()
        
        contents = request_json.get("contents")
        filename = request_json.get("filename")
        
        # process the request
        server_hash = download(filename, contents)
    
    except Exception as e:
        traceback.print_exc()  # print the exception
        return make_response("Invalid request. " + str(e), 400)
    
    # send response
    response_json = {
        "message": f"Successfully stored file {filename}",
        "hash": server_hash
    }
    return jsonify(response_json)
