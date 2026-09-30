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
is_double_digit != book_number
type(book_number)
type(my_guess)
type(is_double_digit)

### Pt. 2 Setup
with open("odyssey.txt", encoding="utf-8") as f:
    text = f.read()






