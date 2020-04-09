T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(M):
        add = list(input().split())
        if add[0] == 'C':
            arr[int(add[1])] = int(add[2])
        elif add[0] == 'D':
            arr.pop(int(add[1]))
        else:
            arr.insert(int(add[1]),int(add[2]))
    if len(arr) < L:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, arr[L]))