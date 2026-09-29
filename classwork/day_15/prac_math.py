x = 50
if x % 2 == 0: print(x, "is even")      # 50 is even
if x % 2 == 0: 
    print(x, "is even.") 
    print("This line only prints if it's even too.") 
print("This line prints no matter what.") 

if x % 2 == 0: 
    print(x, "is even") 
else: 
    print(x, "is odd") 

x = 51
if x % 2 == 0: 
    print(x, "is even") 
else: 
    print(x, "is odd") 

x = 50
if x % 2 == 0:
    print(x, "is even.")
elif x % 2 == 1:
    print(x, "is odd.")
else:
    print(x, "is a decimal.")

x = 51
if x % 2 == 0:
    print(x, "is even.")
elif x % 2 == 1:
    print(x, "is odd.")
else:
    print(x, "is a decimal.")

x = 50.3
if x % 2 == 0:
    print(x, "is even.")
elif x % 2 == 1:
    print(x, "is odd.")
else:
    print(x, "is a decimal.")