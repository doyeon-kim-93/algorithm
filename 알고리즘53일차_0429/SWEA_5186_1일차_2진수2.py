T=int(input())
for tc in range(1,T+1):
    N = float(input())
    cnt = 0
    result = []
    while N:
        if cnt > 12:
            break
        T = N*2
        cnt +=1
        if T >= 1:
            N = T-1
            result += [1]
        else:
            N = T
            result += [0]
    if cnt > 12:
        print('#{} overflow'.format(tc))
    else:
        print('#{}'.format(tc),end = " ")
        print(''.join(map(str,result)))