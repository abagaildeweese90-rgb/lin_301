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

alice_sp = book_to_spacy_df("alice.txt", "Alice", nlp)
alice_sp.head()

alice = book_to_df('alice.txt', "Alice")

print(len(alice))
print(len(alice_sp))

alice_sp["is_ly"] = alice_sp["word"].str.endswith("ly")
alice_sp[alice_sp["is_ly"]].groupby("pos").size().sort_values(ascending=False)

not_adv = alice_sp[alice_sp["is_ly"] & (alice_sp["pos"] != "ADV")]
not_adv.groupby("word").size().sort_values(ascending=False)

adverbs = alice_sp[alice_sp["pos"] == "ADV"]
adverbs.groupby("lemma").size().sort_values(ascending=False).head(10)

content = alice_sp[~alice_sp["is_stop"]]
content.groupby("lemma").size().sort_values(ascending=False).head(10)

alice_sp.head()

alice_sp.loc[[2, 3], "pos"] = "NOUN"
alice_sp.head()

rabbits = alice_sp[alice_sp["word"] == "rabbit"]
rabbits.groupby("pos").size()


mfp_sp = book_to_spacy_df("mansfield_park.txt", "Mansfield Park", nlp)
alice_sp = add_columns(alice_sp, stopwords)   
mfp_sp = add_columns(mfp_sp, stopwords)

alice_sp["is_adv"] = alice_sp["pos"] == "ADV"
mfp_sp["is_adv"] = mfp_sp["pos"] == "ADV"

print(alice_sp["is_adv"].mean() * 1000)
print(alice_sp["is_ly"].mean() * 1000)
print(mfp_sp["is_adv"].mean() * 1000)
print(mfp_sp["is_ly"].mean() * 1000)




