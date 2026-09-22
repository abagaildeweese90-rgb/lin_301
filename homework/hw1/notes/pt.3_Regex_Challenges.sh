grep -Ec "Holmes" holmes.txt #460
grep -Ec "Watson" holmes.txt #81
grep -Ec '\b[a-zA-Z]{5}\b' holmes.txt # 6637
grep -E "\?$" holmes.txt | wc -l #
grep -E "([a-zA-Z]+)\1" holmes.txt | wc -c #465954
grep -E "( he | He | she | She )" holmes.txt | wc -c #92421

# The easiest part of this process for me was the counting and searching aspects because I was there the day we went over it in class. Compared to the navigation aspect which was the hardest because I my computer was acting up that day and I had to learn it myself at home. 
# I think grep and regex would be useful when attempting to locate or countthe amount of a certain phonological accurances in a text. or example, if you were looking for the all instances of 