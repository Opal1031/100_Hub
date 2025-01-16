words = []

for i in range(5):
    word = input()
    words.append(word)

for p in range(15):
    for q in range(5):
        if p < len(words[q]):
            print(words[q][p], end = "")