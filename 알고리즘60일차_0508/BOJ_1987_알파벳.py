dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y, ans):
    global answer
    answer = max(ans, answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and visit[alpha_bo[nx][ny]] == 0:
            visit[alpha_bo[nx][ny]] = 1
            DFS(nx, ny, ans+1)
            visit[alpha_bo[nx][ny]] = 0
R, C = map(int,input().split())
board = [list(input()) for _ in range(R)]
alpha = {'A' : 0,'B' : 1,'C' : 2,'D' : 3,'E' : 4,'F': 5,'G' : 6,'H': 7,'I' : 8,'J': 9,'K': 10,'L' : 11,'M' : 12,'N' : 13,'O' : 14,'P' : 15,'Q' : 16,'R' : 17,'S' : 18,'T' : 19,'U' :20,'V' : 21,'W' : 22,'X' : 23,'Y' : 24,'Z' : 25}
alpha_bo = [[0]*C for _ in range(R)]
visit = [0] * 26
for i in range(R):
    for j in range(C):
        alpha_bo[i][j] = alpha[board[i][j]]
answer = 1
visit[alpha_bo[0][0]] = 1
DFS(0, 0, answer)
print(answer)