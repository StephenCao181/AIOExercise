word = input("Enter a word: ")
result = {}

for character in word:
    if character in result:
        result[character] += 1
    else:
        result[character] = 1

print(result)
