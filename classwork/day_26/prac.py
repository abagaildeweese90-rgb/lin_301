import re
def load_words(filename):
    with open("../../data/gutenberg/" + filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    while not lines[0].startswith("*** START"):
        lines = lines[1:]     # chop off the first line
    lines = lines[1:]         # chop off the *** START line itself

    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]    # chop off the last line
    lines = lines[:-1]        # chop off the *** END line itself

    text = "".join(lines)

    words = re.split(r"[\W]+", text.lower())
    words = [w for w in words if w != ""]
    return words

alice_words = load_words("alice.txt")
print(len(alice_words))

