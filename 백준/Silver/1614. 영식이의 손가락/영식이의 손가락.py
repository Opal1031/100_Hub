dmg_fin = int(input())
count = int(input())

if dmg_fin == 1:
    print(8 * count)

elif dmg_fin == 5:
    print(4 * (count * 2 + 1))

else:
    if (count % 2) == 0:
        print((4 * count) + (dmg_fin - 1))

    else:
        print((4 * count) + (5 - dmg_fin))