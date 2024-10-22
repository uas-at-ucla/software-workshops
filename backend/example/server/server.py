from flask import Flask
from flask import request, make_response, jsonify
import traceback

from backup import backup_and_compute_md5

app = Flask(__name__)


# A POST request is used whenever we change the server's state
# Here we're donwloading a file
@app.route('/backup', methods=["POST"])
def upload():
    try:
        request_json = request.get_json()        
        filename = request_json["filename"]
        
        # process the request
        server_hash = backup_and_compute_md5(filename)
    
    except Exception as e:
        traceback.print_exc()  # print the exception
        return make_response("Invalid request. " + str(e), 400)
    
    # send response
    response_json = {
        "message": f"Successfully stored file {filename}",
        "hash": server_hash
    }
    return jsonify(response_json)
