import sys
sys.stdin = open("input.txt", "r")
dr = [1,-1,0,0]
dc = [0,0,1,-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    che = [0] * ((N**2)+1)
    for i in range(N):
        for j in range(N):
            for z in range(4):
                nr = i + dr[z]
                nc = j + dc[z]
                if 0 <= nr < N and 0 <= nc < N :
                    if room[nr][nc] - room[i][j] == 1:
                        che[room[i][j]] = 1
    cnt = 0
    result = [0,0]
    for i in range(N*N,-1,-1):
        if che[i] == 1:
            cnt += 1
        else:
            if cnt >= result[0]:
                result[0] = cnt
                if 0<= i+1 <= N*N:
                    result[1] = i+1
            cnt = 0

    print('#{} {} {}'.format(tc,result[1],result[0]+1))

