from flask import Flask, request, jsonify, make_response
from backup import backup_and_compute_checksum

app = Flask(__name__)

@app.route("/", methods=['POST'])
def backup():
    try:
        req = request.get_json()
        filename = req['filename']


        response_json = {
            'message': f"Successfully backed up {filename}",
            'checksum': backup_and_compute_checksum(filename)
        }
    except Exception as e:
        response_json = {
            'message': f"Error: {e}",
            'checksum': ""
        }
    
    return jsonify(response_json)
