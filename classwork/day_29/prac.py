import sys
sys.path.append("../../data")
from lin301 import *


alice = book_to_df("alice.txt", "Alice")
alice = add_columns(alice, stopwords)
alice.head()
print(alice.head())
ly_words = alice[alice["is_ly"]]
ly_words.groupby("word").size().sort_values(ascending=False).head(20)

import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("Alice quickly went down the hole, but the only way out was very ugly.")

for token in doc:
    print(token.text)

for token in doc:
    print(token.text, token.lemma_, token.pos_)

doc = nlp("The Queen said that Alice was only a silly little girl.")

for token in doc:
    print(token.text, token.lemma_, token.pos_)

doc = nlp("Alice quickly went down the hole, but the only way out was very ugly.")

rows = []
for token in doc:
    if token.is_alpha:
        rows.append({"word": token.text.lower(),
                     "lemma": token.lemma_.lower(),
                     "pos": token.pos_,
                     "is_stop": token.is_stop})
df = pd.DataFrame(rows)
print(df)
df.groupby("pos").size()
df.groupby("lemma").size()


