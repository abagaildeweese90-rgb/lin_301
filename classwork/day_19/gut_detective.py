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

from itertools import count
import re


hamlet_words = re.split(r"[\W]+", hamlet_text.lower())
hamlet_words = [w for w in hamlet_words if w != ""]
emma_words = re.split(r"[\W]+", emma_text.lower())
emma_words = [w for w in emma_words if w != ""]

print(hamlet_words[0:10])
print(emma_words[0:10])


unique_words = set(hamlet_words)
unique_words = set(emma_words)

tokens = len(hamlet_words)         
types = len(set(hamlet_words))  
print(tokens) #35361
print(types)#5586

text_split = hamlet_text.split()

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr) #0.3

tokens = len(emma_words)         
types = len(set(emma_words))  
print(tokens) #162,095
print(types)  #7255

text_split = emma_text.split()

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr) #0.1

# Even though Hamlet is a shorter text its ttr is higher (0.3%) than Emaa (0.1%).

unique_words = set(hamlet_words)
unique_words = set(emma_words)

tokens = len(hamlet_words [0:10000])         
types = len(set(hamlet_words [0:10000]))  
print(tokens) #10000
print(types) #2427

text_split = hamlet_text.split()

tokens = len(text_split [0:10000])
types = len(set(text_split [0:10000]))

ttr = types/tokens
print(ttr) #0.38

tokens = len(emma_words[0:10000])         
types = len(set(emma_words[0:10000]))  
print(tokens) #10000
print(types) #1783

text_split = emma_text.split()

tokens = len(text_split[0:10000])
types = len(set(text_split[0:10000]))

ttr = types/tokens
print(ttr) #0.26

# So, in the comparison of these two texts its clear that they are outliers in terms of the average comparison but I think in general the second one creates a cotrol variable by having them have the same initial word count because of course on average the longer text will have a higher ttr because you are going to have to use the word the alot more and all other stop words meaning they are less unique.

print(type(hamlet_words))
print(type(emma_words))


hamlet_words = [w for w in hamlet_words if w != ""]
emma_words = [w for w in emma_words if w != ""]

ly_suffix = [w for w in hamlet_words if w.endswith("ly")]
print(len(ly_suffix))

ly_suffix = [w for w in emma_words if w.endswith("ly")]
print(len(ly_suffix))

ness_suffix = [w for w in hamlet_words if w.endswith("ness")]
print(len(ness_suffix))
ness_suffix = [w for w in emma_words if w.endswith("ness")]
print(len(ness_suffix))

ful_suffix = [w for w in hamlet_words if w.endswith("ful")]
print(len(ful_suffix))
ful_suffix = [w for w in emma_words if w.endswith("ful")]
print(len(ful_suffix))

ment_suffix = [w for w in hamlet_words if w.endswith("ment")]
print(len(ment_suffix))
ment_suffix = [w for w in emma_words if w.endswith("ment")]
print(len(ment_suffix))

hamlet_cleaned = [line.strip().lower() for line in book_lines]
emma_cleaned = [line.strip().lower() for line in book_lines]

print(hamlet_cleaned[0:5])
print(emma_cleaned[0:5])