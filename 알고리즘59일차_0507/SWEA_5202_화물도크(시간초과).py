def chek(k):
    global result,con
    if k == N :
        result = max(result,con)
        return
    elif con < result:
        return
    else:
        for i in range(N):
            if disit[i] == 0:
                flag = True
                for z in range(arr2[i][0]+1,arr2[i][1]):
                    if time[z] > 0:
                        flag = False
                        break
                if not flag:
                    disit[i] = 1
                    chek(k+1)
                    disit[i] = 0
                elif flag:
                    disit[i] = 1
                    for y in range(arr2[i][0]+1,arr2[i][1]):
                        time[y] = 1
                    con += 1
                    chek(k+1)
                    con -= 1
                    for y in range(arr2[i][0]+1, arr2[i][1]):
                        time[y] = 0
                    disit[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr2 = sorted(arr)
    time = [0] * 25
    disit = [0] * N
    con = 0
    result = 0
    chek(0)
    print('#{} {}'.format(tc,result))
