words = [
    ["lin", "guis", "tics"],
    ["pho", "no", "lo", "gy"],
    ["mor", "pho", "lo", "gy"],
    ["se", "man", "tics"]
]

total = 0
for syllable in words:
    for syll in syllable:
        print(syll)
        total += 1 

print(total)

for word in words:
    print(word, len(word))
