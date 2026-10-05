words = ["phoneme", "phrase", "morpheme", "reconstruction", "index"]

shouting = [term.strip().lower() for term in words]
print(shouting)

lengths = [len(term) for term in words]
print(lengths)

firsts = [term[0] for term in words]
print(firsts)

mansfield_park = [line.strip().lower() for line in book_lines if line != ""]
print(mansfield_park)

items = ["color", "flavour", "theater", "center", "analyze", "organize", "favorite", "neighbor", "honor", "catalog", "honour", "flavor", "analyse", "flavor", "traveler"]

items = ["color", "flavour", "theater", "center", "analyze", "organize", "favorite", "neighbor", "honor", "catalog", "honour", "flavor", "analyse", "flavor", "traveler"]

r_item_count = 0
for item in items:
    if item[-1] == "r":
        r_item_count += 1
        print(item, r_item_count)

word = "four"
... new_word  = word.replace("our", "or")
... print(new_word)
... 
for
>>> items = ["color", "flavour", "theater", "center", "analyze", "organize", "favor\
ite", "neighbor", "honor", "catalog", "honour", "flavor", "analyse", "flavor", "tra\
veler"]
... 
... down_with_brits = []
... for word in items:
...     if word.endswith("our"):
...         word = word.replace("our", "or")
...     down_with_brits.append(word)
... 
... print(down_with_brits)
... 
['color', 'flavor', 'theater', 'center', 'analyze', 'organize', 'favorite', 'neighbor', 'honor', 'catalog', 'honor', 'flavor', 'analyse', 'flavor', 'traveler']
# Note the .endswith() method - there’s also .startswith()
items = ["color", "flavour", "theater", "center", "analyze", "organize", "favor\
ite", "neighbor", "honor", "catalog", "honour", "flavor", "analyse", "flavor", "tra\
veler"]
... 
... down_with_brits = []
... for word in items:
...     if word.endswith("our"):
...         word = word.replace("our", "or")
        elif word.endswith("yse"):
            word = word.replace("yse", "yze")
...     down_with_brits.append(word)
... 
... print(down_with_brits)

getty = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."

print(getty.split())
      