def chek(k,N):
    global result,choice
    if k == N:
        con = 0
        idx = 0
        for z in range(N):
            con += arr[idx][choice[z]+1]
            idx = choice[z]+1
            if z == N-1:
                con += arr[choice[z]+1][N+1]

        result = min(result,con)
        return
    else:
        for x in range(N):
            if visit[x] == 0:
                visit[x] = 1
                choice.append(x)
                chek(k+1,N)
                visit[x] = 0
                choice.pop()
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    coordinate = list(map(int,input().split()))
    coordinate[2],coordinate[3],coordinate[2*(N+1)],coordinate[2*(N+1)+1] = coordinate[2*(N+1)],coordinate[2*(N+1)+1],coordinate[2],coordinate[3]
    arr = [[0]*(2+N) for _ in range(2+N)]

    for i in range(N+2):
        x = 2*i
        y = 2*i+1
        for j in range(0,N):
            cx = 2*j
            cy = 2*j+1
            if i == 0:
                arr[i][j+1] = abs(coordinate[x]-coordinate[cx+2])+abs(coordinate[y]-coordinate[cy+2])
            elif i == N+1:
                arr[j+1][N+1] = abs(coordinate[x]-coordinate[cx+2])+abs(coordinate[y]-coordinate[cy+2])
            else:
                arr[i][j+1] = abs(coordinate[x]-coordinate[cx+2])+abs(coordinate[y]-coordinate[cy+2])
                
    result = 987654321
    visit = [0]*N
    choice = []
    chek(0,N)
    print('#{} {}'.format(tc,result))