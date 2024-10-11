import hashlib
import requests


def main():

    # read file contents
    with open('ssn.txt', 'rb') as file:
        contents = file.read()

    # send a request to the server
    request_json = {
        "filename": 'ssn.txt',
        "contents": contents
    }    
    response = requests.post("http://localhost:8003/upload", json=request_json)

    # check for changes
    client_hash = hashlib.md5(contents).hexdigest()
    assert response.json()['hash'] == client_hash, "Hashes do not match."

if __name__ == "__main__":
    main()
