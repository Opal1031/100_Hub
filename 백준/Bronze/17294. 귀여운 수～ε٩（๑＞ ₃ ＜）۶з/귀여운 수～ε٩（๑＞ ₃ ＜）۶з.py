Num = list(input())
list = []

for i in range(len(Num) - 1):
    gap = int(Num[i]) - int(Num[i + 1])
    
    if gap not in list:
        list.append(gap)

if len(list) <= 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")