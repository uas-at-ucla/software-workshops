import wget

# put the download inside a function so it is not run when imported
# also make the url a parameter
def download(url):
    wget.download(url)
