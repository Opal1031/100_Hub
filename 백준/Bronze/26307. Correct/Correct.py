Hour, Minute = map(int, input().split())

Diff_Hour = Hour - 9

print(Diff_Hour * 60 + Minute)