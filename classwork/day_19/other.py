hamlet_cleaned = [line.strip().lower() for line in hamlet_lines]
emma_cleaned = [line.strip().lower() for line in emma_lines]

hamlet_nonempty = [line for line in hamlet_cleaned if line != ""]

print(len(hamlet_cleaned) - len(hamlet_nonempty), "empty lines removed")

emma_nonempty = [line for line in emma_cleaned if line != ""]

print(len(emma_cleaned) - len(emma_nonempty), "empty lines removed")

item_count = 0
for item in hamlet_nonempty:
    item_count += 1
    print(item, item_count) # lines: 4225

quote_count = 0
for item in hamlet_nonempty:
    if item[0] == '"' or item[0] == '“' or item[0] == '‘':
        quote_count += 1
        print(item, quote_count) #lines that start with quotes: 7

item_count = 0
for item in emma_nonempty:
    item_count += 1
    print(item, item_count) # lines: 13857

quote_count = 0
for item in emma_nonempty:
    if item[0] == '"' or item[0] == '“' or item[0] == '‘':
        quote_count += 1
        print(item, quote_count) #lines that start with quotes: 1448

# We skip ' because it's and apostrophe and would ruin the data

from collections import Counter

stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t" , '_' ,'footnote', 'chapter', 'mr', 'mrs', 'miss', 
             'ms', 'dr', 'professor', 'sir', 'madam', 'lady', 'lord', 'e', 'r', 'd', 'l', 'h', 'o']

content_words = [w for w in hamlet_words if w not in stopwords]

hamlet_counter = Counter(content_words)
top10 = hamlet_counter.most_common(10)
print(top10)

#[('_ham', 280), ('_i', 154), ('iii', 147), ('hamlet', 126), ('shall', 106), ('c', 103), ('king', 89), ('v', 88), ('thy', 86), ('come', 84)]

# the most common words in hamlet one tell me who the main character is, two tells me that this play is written or takes place in old english, and three is a play so it has odd formating and stage instruction baked into the writing

from collections import Counter

stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t" , '_' ,'footnote', 'chapter', 'mr', 'mrs', 'miss', 'ms', 'dr', 'professor', 'sir', 'madam', 'lady', 'lord',
             'every', 'am', 'well', 'thing']

content_words = [w for w in emma_words if w not in stopwords]

emma_counter = Counter(content_words)
top10 = emma_counter.most_common(10)
print(top10)

#[('emma', 865), ('harriet', 506), ('weston', 439), ('knightley', 389), ('elton', 386), ('think', 383), ('how',371), ('should', 369), ('little', 359), ('good', 359)]

# The top 10 words of Emaa tells me three to four of the main characters and gives some insite into the mundanity of the book

import matplotlib.pyplot as plt

emma_top10 = emma_counter.most_common(10)
hamlet_top10 = hamlet_counter.most_common(10)
emma_content_labels = [pair[0] for pair in emma_top10]
hamlet_content_labels = [pair[0] for pair in hamlet_top10]
emma_content_freqs = [pair[1] for pair in emma_top10]
hamlet_content_freqs = [pair[1] for pair in hamlet_top10]

plt.bar(hamlet_content_labels, hamlet_content_freqs, label="Shakespeare")
plt.bar(emma_content_labels, emma_content_freqs, label="Austin")
plt.title("Top 10 Content Words in Shakespeare vs Austin")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()  
plt.savefig("hamlet_vs_emma_content_top10.png")
plt.legend()
plt.show()

hamlet_freqs = [pair[1] for pair in Counter(hamlet_words).most_common()]
hamlet_ranks = range(1, len(hamlet_freqs) + 1)
emma_freqs = [pair[1] for pair in Counter(emma_words).most_common()]
emma_ranks = range(1, len(emma_freqs) + 1)

plt.plot(hamlet_freqs, hamlet_ranks, label="Shakespeare")
plt.plot(emma_freqs, emma_ranks, label="Austin")
plt.title("Ranks and Frequencies: Shakespeare vs Austin")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale("log")
plt.yscale("log") 
plt.savefig("hamlet_vs_emma_content_top10_line.png")
plt.legend()
plt.show()



