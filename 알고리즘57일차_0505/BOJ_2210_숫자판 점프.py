dr = [1,-1,0,0]
dc = [0,0,1,-1]

def chek(r,c,k):
    global result,con
    if k == 6:
        result.add(''.join(map(str,con)))
        return
    else:
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<5 and 0<=nc<5 and visit[nr][nc] == 0:
                con += [arr[nr][nc]]
                chek(nr,nc,k+1)
                con.pop()

arr = [list(map(int,input().split())) for _ in range(5)]
visit = [[0]*5 for _ in range(5)]
result = set()
for i in range(5):
    for j in range(5):
        con = []
        chek(i,j,0)
print(len(result))


