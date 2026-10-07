import urllib.request

url = "https://www.gutenberg.org/cache/epub/158/pg158.txt"  # Emma
filename = "../../data/gutenberg/emma.txt"

try:
    urllib.request.urlretrieve(url, filename)
    print("Downloaded:", filename)
except FileNotFoundError:
    print("Couldn't save the file — does the ../../data/gutenberg/ folder exist?")