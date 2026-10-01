### Numbers 
books = 24
war_years = 10
journey_years = 10
total_years_away = war_years + journey_years
print(total_years_away)
books_per_week = books // 7
print(books_per_week)
leftover_books = books % 7
print(leftover_books)
#you will need to read 4 books for three weeks and 3 books for 4 weeks to finish all 24 books in 7 weeks.
print(type(books)) #int
print(type(total_years_away)) #int
print(type(books_per_week)) #int

### Strings
hero = "Odysseus"
epithet = "guy who's ego is to big for anyones good"
hero + epithet
print(hero, epithet)
# the plus does not place a space between the two variable and the print version does
homer_quote = "\"the man of twists and turns.\""

### Booleans
war_years == journey_years #true
years_match = war_years == journey_years
print(years_match)
book_number = 9
is_first_book = book_number == 1
is_last_book = book_number == 24
book_number == is_first_book
book_number == is_last_book
is_bookend = is_first_book or is_last_book
print(book_number, is_bookend)

### Book Profile
book_number = 9
my_guess = "Odysessus is mean to a woman and acts super emo over his own choices"
is_double_digit = book_number >= 10
is_double_digit != book_number
type(book_number)
type(my_guess)
type(is_double_digit)

### Pt. 2 Setup
with open("odyssey.txt", encoding="utf-8") as f:
    text = f.read()
words = text.split()

### Lists
print(len(words))
print(words[0:20]) # This is not the real poem these are the first words in the text file.
print(words[50:70]) # not their yet
print(words[100:120]) # nope
print(words[150:170]) # not yet
print(words[250:270]) # This is what it pulled up and I think this is teh preface which I will count because it is not gutenberg. ['“Odyssey”', 'in', 'that', 'book', 'without', 'making', 'it', 'unwieldy,', 'I', 'therefore', 'epitomised', 'my', 'translation,', 'which', 'was', 'already', 'completed', 'and', 'which', 'I']

### Sets
unique_words = set(words)
print(len(unique_words))
len(unique_words) / len(words)
# The type-token ratio of the odessy is alot lower then that of the children stories we previously worked on. This is because the Odyessy is a much longer and more complicated text then the short stories leading to a lot less repeated words. The oyessy also famouly invented/wrote down for the first time new words, so it would make sense that the repetition of words is very low.

### Dictionaries
text.count("Odysseus") #you get the number 
position = text.find("Odysseus")
text[position - 150 : position + 150]
# It turns up seemingly in the middle of the book in the middle of a sentence. 
text.count("Ulysses") #635
#Butler's narrative seemingly relies more on the name Uylsses than Odysseus
character_counts = {"Ulysses": 635,
              "Penelope": 111,
              "Telemachus": 272,
              "Minerva": 152,}
print(character_counts) #{'Ulysses': 635, 'Penelope': 111, 'Telemachus': 272, 'Minerva': 152}
character_counts["Penelope"] #111
character_counts["Telemachus"] #272
character_counts["Minerva"] #152
character_counts["Ulysses"] #635
text.count("Calypso")
character_counts["Calypso"] = 35
print(character_counts) #{'Ulysses': 635, 'Penelope': 111, 'Telemachus': 272, 'Minerva': 152, 'Calypso': 35}

###Part 3 Reflection
# I didn't realise I needed to cd into the folder where the txt file was in bash prior to using python so once I found out it was great.
# I don't think it meaningfully affected the type-token ratio because the text is so long that the 400 max. words added by Gutenberg would have a statiscally tint impact on the ration calculations.
# For me the dict. approach allowed me to find what I needed to the quickest as I had already writen it so I just needed slight adjustments when I ewanted to replecate almost the same results.
