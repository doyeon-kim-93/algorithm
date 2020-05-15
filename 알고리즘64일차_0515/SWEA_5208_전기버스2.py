def chek(k,t):
    global result,cnt
    if k == N:
        result = min(result,cnt)
        return
    elif cnt >= result:
        return
    else:
        for z in range(k,(k+t)+1):
            if z <= N and visit[z] == 0:
                if z == N:
                    visit[z] = 1
                    chek(z,arr[z])
                    visit[z] = 0
                else:
                    visit[z] = 1
                    cnt += 1
                    chek(z,arr[z])
                    cnt -= 1
                    visit[z] = 0

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split())) + [0]
    visit = ([0] * arr[0]) + [0]
    N = arr[0]
    result = 987654321
    cnt = 0
    chek(1,arr[1])
    visit[1] = 1
    print('#{} {}'.format(tc,result))