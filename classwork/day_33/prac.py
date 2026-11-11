import sys
sys.path.append("../../data")
from lin301 import *

import unicodedata
import pandas as pd
from pypinyin import pinyin
import pykakasi
import spacy
import nltk
nltk.download("omw-2.0")
nlp_it = spacy.load("it_core_news_sm")
nlp_zh = spacy.load("zh_core_web_sm")
nlp_ja = spacy.load("ja_core_news_sm")
nlp_el = spacy.load("el_core_news_sm")
nlp_ru = spacy.load("ru_core_news_sm")
nlp_fr = spacy.load("fr_core_news_sm")

for c in "aγж猫はコ":
    print(c, unicodedata.name(c))

def script_of(char):
    return unicodedata.name(char).split()[0]

print(script_of("γ"), script_of("猫"), script_of("は"))

ja = "猫はコウモリを食べるの？"   # 'Do cats eat bats?'

rows = []
for c in ja:
    if c.isalpha():
        rows.append({"char": c, "script": script_of(c)})

pd.DataFrame(rows).groupby("script").size()

el = "Η γάτα κοιμάται στον καναπέ."
ru = "Кошка спит на диване."
ja2 = "猫はソファで寝ます。"

for sentence in [el, ru, ja2]:
    rows = []
    for c in sentence:
        if c.isalpha():
            rows.append({"char": c, "script": script_of(c)})
    print(pd.DataFrame(rows).groupby("script").size().to_dict())

zh = "猫吃蝙蝠吗？"           # 'Do cats eat bats?'
print(zh.split())
print(ja.split())

for token in nlp_zh("猫吃蝙蝠吗？"):
    print(token.text, token.lemma_, token.pos_)

for token in nlp_ja("猫はコウモリを食べるの？"):
    print(token.text, token.lemma_, token.pos_)

for token in nlp_el("Η γάτα τρώει τη νυχτερίδα;"):
    print(token.text, token.lemma_, token.pos_)

for token in nlp_ru("Кошки едят летучих мышей?"):
    print(token.text, token.lemma_, token.pos_)

fr = book_to_spacy_df("alice_fr.txt", "Frence", nlp_it, "CHAPITRE")
it_nouns = fr[fr["pos"] == "NOUN"]

food = wn.synset("food.n.01")
lemmas = it_nouns["lemma"].unique()
fr_food = [lemma for lemma in lemmas if is_a(lemma, food, "ita")]
print(sorted(fr_food))