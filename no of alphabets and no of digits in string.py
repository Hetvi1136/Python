alphabets=0
digits= 0
a = input("enter a string:")
for ch in a:
    if ch.isalpha():
        alphabets+= 1
    elif ch.isdigit():
             digits+= 1


print("number of alphabets:",alphabets)
print("number of digits:",digits)
        
