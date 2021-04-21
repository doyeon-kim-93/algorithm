import sys
sys.stdin = open("input.txt", "r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]
reverse = [1,0,3,2]
def tunnel(k):
    if k == 1:
        return [0,1,2,3]
    elif k == 2:
        return [0,1]
    elif k == 3:
        return [2,3]
    elif k == 4:
        return [0,3]
    elif k == 5:
        return [1,3]
    elif k == 6:
        return [1,2]
    elif k == 7:
        return [0,2]

def check(q):
    global result,pipe
    tmp = []
    while q:
        i,j = q.pop(0)
        move = tunnel(arr[i][j])
        for z in move:
            nr = i + dr[z]
            nc = j + dc[z]
            if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0 and arr[nr][nc] != 0 :
                if reverse[z] in tunnel(arr[nr][nc]):
                    visit[nr][nc] = 1
                    tmp += [(nr,nc)]
                    result += 1
    pipe = tmp[:]
T = int(input())
for tc in range(1,T+1):
    N,M,r,c,t = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 1
    visit = [[0]*M for _ in range(N)]
    pipe = [(r,c)]
    visit[r][c] = 1
    for _ in range(t-1):
        check(pipe)
    print('#{} {}'.format(tc,result))