messy = [" Phoneme\n", "MORPHEME ", "  syntax", "Semantics\n"]

clean = []                            # 1. start with an empty list
for term in messy:                    # 2. go through each item
    clean.append(term.strip().lower())   # 3. add the cleaned version

print(clean)

#or you can
clean = [term.strip().lower() for term in messy]