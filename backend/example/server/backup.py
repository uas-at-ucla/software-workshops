import hashlib

def backup_and_compute_md5(filename):

    # open the original file
    with open(f"../data/{filename}", "rb") as f:
        contents = f.read()

    # backup to another file
    with open(f"backup_data/{filename}", "wb") as f:
        f.write(contents)

    # compute the MD5 of the file contents and return it
    return hashlib.md5(contents).hexdigest()
    