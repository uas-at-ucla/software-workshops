import hashlib

def download(filename, contents):

    # save the file
    with open(filename, "w") as file:
        file.write(contents)

    # compute the MD5 of the file contents and return it
    return hashlib.md5(str.encode(contents)).hexdigest()
    