import sys
sys.setrecursionlimit(1000000)
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def nomal(r,c,k):
    for z in range(4):
        nr = r + dr[z]
        nc = c + dc[z]
        if 0<= nr <N and 0<= nc < N :
            if arr[nr][nc] == k :
                con.append(arr[nr][nc])
                arr[nr][nc] = '1'
                nomal(nr,nc,k)
def eye(r,c,k):
    for z in range(4):
        nr = r + dr[z]
        nc = c + dc[z]
        if 0<= nr <N and 0<= nc < N :
            if arr2[nr][nc] == k :
                con2.append(arr2[nr][nc])
                arr2[nr][nc] = '1'
                eye(nr,nc,k)

N = int(input())
arr = [list(map(str,input())) for _ in range(N)]
arr2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr2[i][j] = 'R'
        else:
            arr2[i][j] = arr[i][j]
color = ['R','B','G']
result_nomal = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            con = []
            nomal(i,j,'R')
            result_nomal.append(con)
        elif arr[i][j] == 'B':
            con = []
            nomal(i,j,'B')
            result_nomal.append(con)
        elif arr[i][j] == 'G':
            con = []
            nomal(i,j,'G')
            result_nomal.append(con)
result_eye = []
for i in range(N):
    for j in range(N):
        if arr2[i][j] == 'R':
            con2 = []
            eye(i, j, 'R')
            result_eye.append(con2)
        elif arr2[i][j] == 'B':
            con2 = []
            eye(i, j, 'B')
            result_eye.append(con2)
print(len(result_nomal),end = ' ')
print(len(result_eye),end = '')