dr = [1,-1,0,0]
dc = [0,0,1,-1]

def chek(r,c,k):
    global result,con
    if k == 7:
        cnt2 = 0
        for x in range(7):
            if con[x][0] == 'S':
                cnt2 +=1
        if cnt2 >= 4:
            result.add(''.join(map(str,con)))
            return
    else:
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<5 and 0<=nc<5 and visit[nr][nc] == 0:
                visit[nr][nc] = 1
                con += [arr2[nr][nc]]
                chek(nr,nc,k+1)
                visit[nr][nc] = 0
                con.pop()

arr = [list(input()) for _ in range(5)]
cnt = 0
arr2 = [[(0,0)]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        arr2[i][j] = (arr[i][j],cnt)
        cnt += 1
visit = [[0]*5 for _ in range(5)]
result = set()
for i in range(5):
    for j in range(5):
        con = []
        visit[i][j] = 1
        chek(i,j,0)
        visit[i][j] = 0
print(result)
print(len(result))



