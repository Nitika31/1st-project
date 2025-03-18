string = input("Enter a string: ")
if len(string) >= 3:
    if string.endswith('ing'):
        print(f"{string}ly")
    else:
        print(f"{string}ing")
else:
    print(string)
