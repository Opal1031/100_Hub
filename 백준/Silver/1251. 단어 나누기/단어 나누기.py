word = input()
answer = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = "".join(reversed(word[:i]))
        second = "".join(reversed(word[i:j]))
        third = "".join(reversed(word[j:]))

        answer.append(first + second + third)

print(sorted(answer)[0])