string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
swapped_string = string2[:2] + string1[2:] + " " + string1[:2] + string2[2:]
print(f"Swapped string: {swapped_string}")
