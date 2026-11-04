import sys
sys.path.append("../../data")
from lin301 import *

import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("I am delighted to be here today. We meet in an hour of change and challenge. Do cats eat bats?")

for sent in doc.sents:
    print(sent.text)

alice_sp = book_to_spacy_df("alice.txt", "Alice", nlp)
print(alice_sp.head())

lengths = alice_sp.groupby(["chapter", "sentence"]).size()
print(lengths.head())

avg_len = alice_sp.groupby(["chapter", "sentence"]).size().mean()
print(avg_len)

#mfp_sp = book_to_spacy_df("mansfield_park.txt", "Mansfield Park", nlp)

#avg_len = mfp_sp.groupby(["chapter", "sentence"]).size().mean()
#print(avg_len)
#Austen

doc = nlp("Do cats eat bats?")

for token in doc:
    print(token.text, token.dep_, token.head.text)

doc = nlp("Do cats eat bats?")

for token in doc:
    print(token.text, token.dep_, token.head.text)

doc = nlp("Do cats eat bats?")
svg = displacy.render(doc, style="dep")
with open("cats_eat_bats.svg", "w", encoding="utf-8") as f:
    f.write(svg)

doc = nlp("Do bats eat cats?")
svg = displacy.render(doc, style="dep")
with open("bats_eat_cats.svg", "w", encoding="utf-8") as f:
    f.write(svg)

doc = nlp("The Hatter dropped his teacup on the floor.")
for token in doc:
    print(token.text, token.dep_, [child.text for child in token.children])
svg = displacy.render(doc, style="dep")
with open("hatter_teacup.svg", "w", encoding="utf-8") as f:
    f.write(svg)

alice_svo = book_to_svo_df("alice.txt", "Alice", nlp)
alice_svo.head()

alice_svo.groupby("verb").size().sort_values(ascending=False).head(10)

queen = alice_svo[alice_svo["subject"] == "queen"]
print(queen.groupby("verb").size().sort_values(ascending=False).head(8))

hatter = alice_svo[alice_svo["subject"] == "hatter"]
print(hatter.groupby("verb").size().sort_values(ascending=False).head(8))

rabbit = alice_svo[alice_svo["subject"] == "rabbit"]
print(rabbit.groupby("verb").size().sort_values(ascending=False).head(8))

people = ["queen", "hatter", "rabbit", "alice", "cat", "caterpillar", "march hare", "doremouse",]

print(alice_svo[alice_svo["object"].isin(people)])