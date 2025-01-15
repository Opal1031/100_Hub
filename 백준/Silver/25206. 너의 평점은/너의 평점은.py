grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total_score = 0
total_credit = 0


for i in range(20):
    subject = list(map(str, input().split()))
    credit = float(subject[1])

    if subject[2] == "P":
        continue
    
    index = grade_list.index(subject[2])
    score = score_list[index]
    total_score += (credit * score)
    total_credit += credit

avg = float(total_score / total_credit)
print(avg)