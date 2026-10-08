import urllib.request

url = "https://www.gutenberg.org/cache/epub/158/pg158.txt"  # Emma
filename = "../../data/gutenberg/emma.txt"


try:
    with open("../../data/gutenberg/emma.txt", "r", encoding="utf-8") as f:
        emma_lines = f.readlines()
except FileNotFoundError:
    print("File not found — does the ../../data/gutenberg/ folder exist?")

while not emma_lines[0].startswith("*** START"):
    emma_lines = emma_lines[1:]     # chop off the first line
emma_lines = emma_lines[1:]         # chop off the *** START line itself

print(emma_lines[0:5])

while not emma_lines[-1].startswith("*** END"):
    emma_lines = emma_lines[:-1]    # chop off the last line
emma_lines = emma_lines[:-1]        # chop off the *** END line itself

emma_text = "".join(emma_lines)

print(emma_lines[-5:])

emma_text = "".join(emma_lines)   # glue the lines back together into a string

import re

emma_words = re.split(r"[\W]+", emma_text.lower())
emma_words = [w for w in emma_words if w != ""]

text_split = emma_text.split()

unique_words = set(emma_words)

tokens = len(emma_words)         
types = len(set(emma_words))  
print(tokens)
print(types)

text_split = emma_text.split()

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr)