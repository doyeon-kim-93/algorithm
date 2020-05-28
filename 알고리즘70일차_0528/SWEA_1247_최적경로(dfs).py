def chek(n,s,con):
    global result
    if con > result:
        return
    if n == N:
        L = abs(s[0]-end[0])+abs(s[1]-end[1])
        result = min(result,con+L)
        return
    else:
        for z in range(N):
            if visit[z] == 0:
                visit[z] = 1
                L = abs(s[0]-client[z][0])+abs(s[1]-client[z][1])
                chek(n+1,client[z],con+L)
                visit[z] = 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    coo = list(map(int,input().split()))
    start = (coo[0],coo[1])
    end = (coo[2],coo[3])
    client = []
    for i in range(4,len(coo),2):
        client.append((coo[i],coo[i+1]))

    visit = [0] * N
    result = 987654321
    chek(0,start,0)
    print('#{} {}'.format(tc, result))