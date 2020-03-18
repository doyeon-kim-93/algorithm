def plus(k):
    if not k:
        return 0
    if k == 1:
        return 1
    if k == 2:
        return 3
    if k >2:
        return plus(k-1) + (2*plus(k-2))

T = int(input())
for tc in range(1,T+1):
    N = int(input())//10
    print('#{} {}'.format(tc,plus(N)))