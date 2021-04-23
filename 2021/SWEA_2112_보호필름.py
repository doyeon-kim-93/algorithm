import sys
sys.stdin = open("input.txt", "r")

def check(arr):
    global D,W,K
    flag = [0]*W
    for j in range(W):
        cnt = 0
        sp = -1
        for i in range(D):
            if sp == -1:
                sp = arr[i][j]
                cnt += 1
                if cnt == K:
                    flag[j] = 1
                    break
            else:
                if sp == arr[i][j]:
                    cnt += 1
                    if cnt == K:
                        flag[j] = 1
                        break
                else:
                    sp = arr[i][j]
                    cnt = 1
        if flag[j] == 0:
            return False
    if sum(flag) == W:
        return True
    else:
        return False

def medicine(idx,con,n):
    global visitM,result
    if idx == n:
        tmp = [arr2[i][:] for i in range(D)]
        cost = 0
        for z,val in enumerate(visitM):
            if val == 0:
                tmp[z][:] = [0]*W
                cost += 1
            elif val == 1:
                tmp[z][:] = [1]*W
                cost += 1
        if check(tmp):
            result = min(result,cost)
        return
    if con >= result:
        return
    for i in range(2):
        visitM[idx] = i
        medicine(idx+1,con+1,n)
    visitM[idx] = -1
    medicine(idx+1,con,n)

T = int(input())
for tc in range(1,T+1):
    D,W,K = map(int,input().split())
    arr2 = [list(map(int,input().split())) for _ in range(D)]
    result = 987654321
    if check(arr2):
        print('#{} {}'.format(tc, 0))
    else:
        visitM = [-1]*D
        medicine(0,0,D)
        print('#{} {}'.format(tc,result))