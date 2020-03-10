from collections import deque
dr = [1,-1,0,1]
dc = [0,0,1,1]
def bfs(r1,c1,cnt1,w,index):
    global q,point
    q += [(r1,c1,cnt1)]
    arr[r1][c1] = 4
    while q:
        r,c,cnt = q.popleft()
        if result[index]<cnt:
            result[index] +=1
        elif result[index] > cnt:
            continue
        flag = False
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<= nr < H and 0 <=nc < w+1:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 1
                    q += [(nr,nc,cnt+1)]
                elif arr[nr][nc] == 3:
                    result[i] += 1
                    flag = True
                    break
        if flag:
            break
T = int(input())
for tc in range(1,T+1):
    W, H, N = map(int,input().split())
    arr = [[0]*W for _ in range(H)]
    result = [0] * (N-1)
    point = []
    for _ in range(N):
        j,i = map(int,input().split())
        arr[i-1][j-1] = 3
        point += [(i-1,j-1,0)]
    for i in range(N-1):
        q = deque([])
        bfs(*point[i],point[i+1][1],i)
    print("#{} {}".format(tc,sum(result)))
    print(result)
    for z in range(H):
        print(arr[z])
