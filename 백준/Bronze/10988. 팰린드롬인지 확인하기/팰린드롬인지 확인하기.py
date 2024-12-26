word = input()

word_reverse = "".join(reversed(word[0:]))

if word == word_reverse:
    print("1")
else:
    print("0")