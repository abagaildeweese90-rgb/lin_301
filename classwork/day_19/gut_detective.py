# import urllib.request

#url = "https://www.gutenberg.org/cache/epub/27761/pg27761.txt"  # Hamlet
#filename = "../../data/gutenberg/hamlet.txt"

#try:
    #urllib.request.urlretrieve(url, filename)
    #print("Downloaded:", filename)
#except FileNotFoundError:
   # print("Couldn't save the file — does the ../../data/gutenberg/ folder exist?")

try:
    with open("../../data/gutenberg/hamlet.txt", "r", encoding="utf-8") as f:
        hamlet_lines = f.readlines()
except FileNotFoundError:
    print("File not found — does the ../../data/gutenberg/ folder exist?")

while not hamlet_lines[0].startswith("*** START"):
    hamlet_lines = hamlet_lines[1:]     # chop off the first line
hamlet_lines = hamlet_lines[1:]         # chop off the *** START line itself

print(hamlet_lines[0:5])

while not hamlet_lines[-1].startswith("*** END"):
    hamlet_lines = hamlet_lines[:-1]    # chop off the last line
hamlet_lines = hamlet_lines[:-1]        # chop off the *** END line itself

hamlet_text = "".join(hamlet_lines)

print(hamlet_lines[-5:])

hamlet_text = "".join(hamlet_lines)   # glue the lines back together into a string

import re


hamlet_words = re.split(r"[\W]+", hamlet_text.lower())
hamlet_words = [w for w in hamlet_words if w != ""]

unique_words = set(hamlet_words)

tokens = len(hamlet_words)         
types = len(set(hamlet_words))  
print(tokens)
print(types)

text_split = hamlet_text.split()

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr)
