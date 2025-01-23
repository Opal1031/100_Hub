Test = int(input())

for i in range(Test):
    Tel_L, Tel_W, Eur_L, Eur_W = map(int, input().split())

    Tel_S = Tel_L * Tel_W
    Eur_S = Eur_L * Eur_W

    if Tel_S > Eur_S:
        print("TelecomParisTech")
    elif Tel_S == Eur_S:
        print("Tie")
    else:
        print("Eurecom")