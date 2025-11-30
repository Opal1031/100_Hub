da_long = ["C", "F", "G"]
ga_short = ["A", "D", "E"]

music = input().split('|')

da_cnt = 0
ga_cnt = 0
last = music[-1][-1]

for i in music:
    if i[0] in da_long:
        da_cnt += 1
    if i[0] in ga_short:
        ga_cnt += 1


if da_cnt == ga_cnt:
    if last in da_long:
        da_cnt += 1
    if last in ga_short:
        ga_cnt += 1

if da_cnt > ga_cnt:
    print("C-major")
else:
    print("A-minor")