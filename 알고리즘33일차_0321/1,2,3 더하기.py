def che(k):
    if k == 0:
        return 1
    elif k == 1 :
        return 1
    elif k == 2:
        return 2
    elif k == 3:
        return 4
    else:
        return che(k-1) + che(k-2) + che(k-3)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(che(N))
