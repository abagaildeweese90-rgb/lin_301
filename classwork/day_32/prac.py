import sys
sys.path.append("../../data")
from lin301 import *

import unicodedata
import spacy
nlp = spacy.load("en_core_web_sm")
nlp_fr = spacy.load("fr_core_news_sm")
nlp_it = spacy.load("it_core_news_sm")

en = book_to_spacy_df("alice.txt", "English", nlp)
fr = book_to_spacy_df("alice_fr.txt", "French", nlp_fr, "CHAPITRE")
it = book_to_spacy_df("alice_it.txt", "Italian", nlp_it, "CAPITOLO")

for df in [en, fr, it]:
    print(df["text"][0], len(df), df["chapter"].max())