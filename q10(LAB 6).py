words = ['apple', 'banana', 'cat', 'elephant']
n = 3

result = []
for word in words:
    if len(word) > n:
        result.append(word)

print("Words longer than", n, "characters are:", result)
