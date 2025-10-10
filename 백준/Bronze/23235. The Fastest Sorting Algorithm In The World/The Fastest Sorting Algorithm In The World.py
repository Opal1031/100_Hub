import sys
input = sys.stdin.readline

case_number = 1

while True:
    line = list(map(int, input().split()))

    if (line[0] == 0):
        break
    
    print(f'Case {case_number}: Sorting... done!')

    case_number += 1