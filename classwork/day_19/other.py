import urllib.request

url = "https://www.gutenberg.org/cache/epub/158/pg158.txt"  # Emma
filename = "../../data/gutenberg/emma.txt"



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


unique_words = set(emma_words)

tokens = len(emma_words)         
types = len(set(emma_words))  
print(tokens)
print(types)

text_split = emma_text.split()


ttr = types/tokens
print(ttr)

from collections import Counter
import matplotlib.pyplot as plt

book1_freqs = [pair[1] for pair in Counter(emma_words).most_common()]
book1_ranks = range(1, len(book1_freqs) + 1)    # 1, 2, 3, ... up to the number of words

plt.plot(book1_ranks, book1_freqs)
plt.title("Rank vs. Frequency")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.show()