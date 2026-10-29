words = ['apple', 'ant', 'banana', 'ball', 'cat']

result = {}

for word in words:
    first_char = word[0]

    if first_char in result:
        result[first_char].append(word)
    else:
        result[first_char] = [word]

print(result)