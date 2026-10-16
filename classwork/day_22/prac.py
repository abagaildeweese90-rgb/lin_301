consonant =  ["p", "b", "t", "d", "k", "g", "s", "z", "m", "n", "l", "r", "w", "j", "h"]
place = ["bilabial", "bilabial", "alveolar", "alveolar", "velar", "velar", "alveolar", "alveolar", "bilabial", "alveolar", "alveolar", "alveolar", "labial-velar", "palatal", "glottal"]
manner = ["stop", "stop", "stop", "stop", "stop", "stop", "fricative", "fricative", "nasal", "nasal", "lateral", "trill", "glide", "glide", "fricative"]
voice = ["voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiceless"]

consonants = {}

for c, pl, m, v in zip(consonant, place, manner, voice):
    consonants[c] = {"place": pl, "manner": m, "voice": v}

print(consonants)

print(consonants["j"]["place"])

