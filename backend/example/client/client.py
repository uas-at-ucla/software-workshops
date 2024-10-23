import requests
import hashlib

def main():
    filename = 'ssn.txt'

    response = requests.post('http://localhost:5000', json={'filename': filename})
    response_json = response.json()

    # open the file
    with open(f"../data/{filename}", 'rb') as f:
        contents = f.read()

    # compare the checksums
    local_checksum = hashlib.md5(contents).hexdigest()
    print(local_checksum)

    if local_checksum == response_json['checksum']:
        print('Success')
    else:
        print(response_json)

main()