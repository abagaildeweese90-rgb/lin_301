sisters = ["Charlotte", "Emily", "Anne", "Charlotte", "Emily", "Charlotte"]

unique_sisters = set(sisters)
print(unique_sisters)
# {'Charlotte', 'Emily', 'Anne'}  -- order not guaranteed!

unique_sisters.add("Branwell")
"Emily" in unique_sisters       # fast membership check

jane_eyre_vocab = {"orphan", "governess", "moor", "fire", "love"}
wuthering_heights_vocab = {"moor", "ghost", "revenge", "love", "storm"}

jane_eyre_vocab | wuthering_heights_vocab   # union: either novel
jane_eyre_vocab & wuthering_heights_vocab   # intersection: both novels
jane_eyre_vocab - wuthering_heights_vocab   # difference: only Jane Eyre

with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:  # opens alice.txt for reading
    text = f.read()                                           # reads the whole file into one string, called `text`

text_split = text.split()