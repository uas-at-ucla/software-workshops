import hashlib
import requests


def main():
    filename = 'ssn.txt'

    # send a request to the server
    request_json = {
        "filename": filename
    }    
    response = requests.post("http://localhost:5000/backup", json=request_json)

    # check for changes
    with open(f'../data/{filename}', 'rb') as f:
        contents = f.read()

    client_hash = hashlib.md5(contents).hexdigest()
    assert response.json()['hash'] == client_hash, "Hashes do not match."

    print("Success")

if __name__ == "__main__":
    main()
