import hashlib

def backup_and_compute_checksum(filename):
    # open the file
    with open(f"../data/{filename}", 'rb') as f:
        contents = f.read()

    # save the contents
    with open(f"backup_data/{filename}", 'wb') as f:
        f.write(contents)

    # return checksum
    return hashlib.md5(contents).hexdigest()