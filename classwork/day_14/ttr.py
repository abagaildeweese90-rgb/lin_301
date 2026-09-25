with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:  # opens alice.txt for reading
    text = f.read()                                           # reads the whole file into one string, called `text`

text_split = text.split()
print(text_split[:100])  # prints the first 10 words in the text