import sys
sys.stdin = open("input (2).txt", "r")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dr = [0,1]
    dc = [1,0]
    result1 = []
    for i in range(N):
        for j in range(N):
            w = 0
            l = 0
            if arr[i][j] != 0:
                r = i
                c = j
                while 1:
                    nr = r + dr[0]
                    nc = c + dc[0]
                    if 0<=nr<N and 0<=nc<N and arr[nr][nc] != 0:
                        w += 1
                        r = nr
                        c = nc
                    else:
                        r = i
                        c = j
                        break
                while 1:
                    nr = r + dr[1]
                    nc = c + dc[1]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0:
                        l += 1
                        r = nr
                        c = nc
                    else:
                        break
            for y in range(i,i+l+1):
                for x in range(j,j+w+1):
                        arr[y][x] = 0
            if w != 0 or l != 0:
                result1.append([l+1,w+1])
    # print(result1)
    result2 = []
    for i in range(len(result1)):
        mul = result1[i][0]*result1[i][1]
        result2.append([mul,result1[i][0],result1[i][1]])
    result2.sort()
    N_re =len(result2)
    print('#{} {}'.format(tc,N_re),end=' ')
    for z in range(N_re):
        print('{} {}'.format(result2[z][1],result2[z][2]),end= ' ')
    print('\b')
