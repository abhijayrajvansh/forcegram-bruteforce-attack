from dis import dis


dictionary = []
with open('dictionary.txt', 'r') as file:
    for words in file:
        words = words.strip()
        dictionary.append(words)

i = 0
while True:
    print(dictionary[i])
    i += 1