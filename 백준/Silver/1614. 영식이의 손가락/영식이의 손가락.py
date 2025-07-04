dmg_fin = int(input())
use_dmg_fin = int(input())

if dmg_fin == 1:
    print(8 * use_dmg_fin)

elif dmg_fin == 5:
    print(4 * (use_dmg_fin * 2 + 1))

else:
    if (use_dmg_fin % 2) == 0:
        print((4 * use_dmg_fin) + (dmg_fin - 1))
    
    else:
        print((4 * use_dmg_fin) + (5 - dmg_fin))