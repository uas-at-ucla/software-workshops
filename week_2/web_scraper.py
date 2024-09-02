import wget

# put the download inside a function so it is not run when imported
# also make the url a parameter
def download(url):
    wget.download(url)

if __name__ == "__main__":  # this is like the entrypoint of the script
    download()