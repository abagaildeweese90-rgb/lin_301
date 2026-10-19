import re
import pandas as pd

with open("../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
    alice_lines = f.readlines()

while not alice_lines[0].startswith("*** START"):
    alice_lines = alice_lines[1:]
alice_lines = alice_lines[1:]

while not alice_lines[-1].startswith("*** END"):
    alice_lines = alice_lines[:-1]
alice_lines = alice_lines[:-1]

alice_text = "".join(alice_lines)

import re

chapters = re.split(r"\nCHAPTER [IVXL]+", alice_text)
print(len(chapters))

print(chapters[0])

chapters = chapters[1:]
print(len(chapters))

print(chapters[0])

rows = []
chapter_num = 0

for chapter in chapters:
    chapter_num += 1
    words = re.split(r"[\W]+", chapter.lower())
    words = [w for w in words if w != ""]
    for w in words:
        rows.append({"word": w, "chapter": chapter_num})

alice_df = pd.DataFrame(rows)

print(len(alice_df)) #27324

print(alice_df.head(30))

words = alice_df["word"]
len_words = len(words)


print(alice_df[alice_df["word"] == "queen"])

print(len(alice_df[alice_df["word"] == "alice"])) #396

print(alice_df[alice_df["word"].str.endswith("ing")])

un = alice_df[alice_df["word"].str.startswith("un")]
un = un[un["word"] != "under"]

print(alice_df[alice_df["word"].str.startswith("un") & (alice_df["chapter"] == 1)])

print(len(alice_df[(alice_df["word"].isin(["king", "queen"])) & (alice_df["chapter"] == 12)]))

stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t"]

content = alice_df[~alice_df["word"].isin(stopwords)]

print(content)



