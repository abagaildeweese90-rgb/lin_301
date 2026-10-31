import re
import pandas as pd

# Stopwords (from Day 18)
stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t"]

# 1. Load Alice and cut off the Gutenberg header and footer
with open("../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
    alice_lines = f.readlines()

while not alice_lines[0].startswith("*** START"):
    alice_lines = alice_lines[1:]
alice_lines = alice_lines[1:]

while not alice_lines[-1].startswith("*** END"):
    alice_lines = alice_lines[:-1]
alice_lines = alice_lines[:-1]

alice_text = "".join(alice_lines)

# 2. Split into chapters (and drop everything before Chapter I)
chapters = re.split(r"\nCHAPTER [IVXL]+", alice_text)
chapters = chapters[1:]

# 3. One row per word, with its chapter
rows = []
chapter_num = 0

for chapter in chapters:
    chapter_num += 1
    words = re.split(r"[\W_]+", chapter.lower())   # split on \W AND on _
    words = [w for w in words if w != ""]
    for w in words:
        rows.append({"word": w, "chapter": chapter_num})

alice_df = pd.DataFrame(rows)

print(alice_df.head()) #prints the first 5 rows
print(alice_df.tail()) #prints the last 5 rows
print(len(alice_df)) #prints the num. of words in the data frame
print(alice_df.columns) #prints the columns
