import sys
sys.stdin = open("input.txt", "r")

dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]
re = [0,2,1,4,3]

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]
    for _ in range(M):
        point = []
        union = set()
        arrmap = [[[] for _ in range(N)] for _ in range(N)]
        for z in range(K):
            r = arr[z][0] + dr[arr[z][3]]
            c = arr[z][1] + dc[arr[z][3]]
            if 0<=r<N and 0<=c<N:
                arr[z][0], arr[z][1] = r, c
                arrmap[r][c].append(z)
                if (r,c) in point:
                    union.add((r,c))
                else:
                    point.append((r,c))
                if r == 0 or r == N - 1 or c == 0 or c == N - 1:
                    arr[z][3] = re[arr[z][3]]
        for i,j in point:
            if (i,j) not in union:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    arr[arrmap[i][j][0]][2] = int(arr[arrmap[i][j][0]][2]/2)
        for i,j in union:
            idx = 0
            value = 0
            sum_value = 0
            for z in arrmap[i][j]:
                if arr[z][2] > value:
                    value = arr[z][2]
                    idx = z
                sum_value += arr[z][2]
            if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                arr[idx][2] = int(sum_value/2)
            else:
                arr[idx][2] = sum_value
            for x in arrmap[i][j]:
                if x != idx:
                    arr[x][0],arr[x][1],arr[x][2],arr[x][3] = -1,-1,0,0
    result = 0
    for i in range(K):
        result += arr[i][2]
    print('#{} {}'.format(tc,result))