variable = input("Input multiple words as one word with the first letter of each word being uppercase: ")

for i in variable:
    if i.isupper():
        print("_", i.lower(), end="")
    else:
        print(i, end="")