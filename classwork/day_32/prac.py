import sys
sys.path.append("../../data")
from lin301 import *

import unicodedata
import spacy
nlp = spacy.load("en_core_web_sm")
nlp_fr = spacy.load("fr_core_news_sm")
nlp_it = spacy.load("it_core_news_sm")

doc = nlp_it("I gatti mangiano i pipistrelli?")

for token in doc:
    print(token.text, token.lemma_, token.pos_)

doc = nlp_it("Alice cominciava a sentirsi stanca.")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.morph)
    
