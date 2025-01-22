Test = int(input())

for i in range(Test):
    list = input()

    Sum_score = 0
    score = 0

    for j in list:
        if j == "O":
            score += 1
        else:
            score = 0
        Sum_score += score

    print(Sum_score)