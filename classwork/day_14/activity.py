austen_opening = ["it", "is", "a", "truth", "universally", "acknowledged", "that", "a",
                   "single", "man", "in", "possession", "of", "a", "good", "fortune",
                   "must", "be", "in", "want", "of", "a", "wife"]

bronte_opening = ["there", "was", "no", "possibility", "of", "taking", "a", "walk",
                   "that", "day", "we", "had", "been", "wandering", "in", "the",
                   "leafless", "shrubbery", "an", "hour", "in", "the", "morning"]

# Austen
print(len(austen_opening))            # 23 tokens
print(len(set(austen_opening)))       # 18 types
print(len(set(austen_opening)) / len(austen_opening))   # TTR ~ 0.78

# Bronte
print(len(bronte_opening))            # 23 tokens
print(len(set(bronte_opening)))       # 21 types
print(len(set(bronte_opening)) / len(bronte_opening))   # TTR ~ 0.91

austen_words = set(austen_opening)
bronte_words = set(bronte_opening)

print(austen_words & bronte_words)
# {'a', 'in', 'of', 'that'}   -- small function words, not content words

print(austen_words - bronte_words)
# the 14 words unique to the Austen passage

print(austen_opening.count("a"))   # 4
print("a" in austen_words)         # True -- but that's all a set can tell you