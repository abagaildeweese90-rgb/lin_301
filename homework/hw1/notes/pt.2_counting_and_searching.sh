wc holmes.txt # 12310  107558 607606
wc -l holmes.txt # 12310
wc -w holmes.txt # 107558
grep "Watson" holmes.txt | wc -l # 81
grep "Holmes" holmes.txt | wc -l # 460
# Holmes appears more than Watson.
