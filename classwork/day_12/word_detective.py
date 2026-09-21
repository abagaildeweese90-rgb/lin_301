word = input("Enter a word any word:")
first_letter_a = word[0] == "a"
first_letter_e = word[0] == "e"
first_letter_i = word[0] == "i"
first_letter_o = word[0] == "o"
first_letter_u = word[0] == "u"

is_vowel = first_letter_a or first_letter_e or first_letter_i or first_letter_o or first_letter_u

print("The first letter of your word is a vowel:", is_vowel)
first_novel = "Sense and Sensibility"
novels = ["Sense and Sensibility", "Pride and Prejudice", "Mansfield Park", "Emma", "Northanger Abbey", "Persuasion", "Lady Susan"]
print(novels)