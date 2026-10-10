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

try:
    with open("../../data/gutenberg/emma.txt", "r", encoding="utf-8") as f:
        emma_lines = f.readlines()
except FileNotFoundError:
    print("File not found — does the ../../data/gutenberg/ folder exist?")

while not hamlet_lines[0].startswith("*** START"):
    hamlet_lines = hamlet_lines[1:]     # chop off the first line
hamlet_lines = hamlet_lines[1:]         # chop off the *** START line itself

while not emma_lines[0].startswith("*** START"):
    emma_lines = emma_lines[1:]     # chop off the first line
emma_lines = emma_lines[1:]         # chop off the *** START line itself

print(hamlet_lines[0:5])
print(emma_lines[0:5])

while not hamlet_lines[-1].startswith("*** END"):
    hamlet_lines = hamlet_lines[:-1]    # chop off the last line
hamlet_lines = hamlet_lines[:-1]        # chop off the *** END line itself

while not emma_lines[-1].startswith("*** END"):
    emma_lines = emma_lines[:-1]    # chop off the last line
emma_lines = emma_lines[:-1]        # chop off the *** END line itself

hamlet_text = "".join(hamlet_lines)
emma_text = "".join(emma_lines)

print(hamlet_lines[-5:])
print(emma_lines[-5:])

import re


hamlet_words = re.split(r"[\W]+", hamlet_text.lower())
hamlet_words = [w for w in hamlet_words if w != ""]
emma_words = re.split(r"[\W]+", emma_text.lower())
emma_words = [w for w in emma_words if w != ""]


unique_words = set(hamlet_words)
unique_words = set(emma_words)

tokens = len(hamlet_words)         
types = len(set(hamlet_words))  
print(tokens)
print(types)

text_split = hamlet_text.split()

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr)

tokens = len(emma_words)         
types = len(set(emma_words))  
print(tokens)
print(types)

text_split = emma_text.split()

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr)

# Even though Hamlet is a shorter text its ttr is higher (0.3%) than Emaa (0.1%).

unique_words = set(hamlet_words)
unique_words = set(emma_words)

tokens = len(hamlet_words)         
types = len(set(hamlet_words))  
print(tokens)
print(types)

text_split = hamlet_text.split()

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr)

tokens = len(emma_words)         
types = len(set(emma_words))  
print(tokens)
print(types)

text_split = emma_text.split()

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr)