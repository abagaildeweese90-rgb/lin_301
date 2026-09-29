vowels = ["a", "e", "i", "o", "u"]
consonants = ["p", "t", "k", "m", "n", "s", "r", "l"]

sound = "p"
if sound in vowels:
    print(sound, "is a vowel.")
elif sound in consonants:
    print(sound, "is a consonant.")
else:
    print(sound, "is neither a vowel nor a consonant.")