def chek(k,li):
    global result
    before = 0
    current = 2
    l = 0
    r = len(li) - 1
    while l <= r:
        m = (l + r) // 2
        if k == li[m]:
            result += 1
            break
        elif k < li[m]:
            r = m - 1
            current = -1
        elif k > li[m]:
            l = m + 1
            current = 1
        if before == current:
            break
        before = current

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    result = 0
    num = []
    flag = True
    for i in A:
        if i in B:
            num += [i]
    if len(num) == 0:
        flag = False
    if flag:
        for z in num:
            turn = 0
            chek(z,A)
    print('#{} {}'.format(tc,result))