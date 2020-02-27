import sys
sys.setrecursionlimit(100000)
def bfs(n,k):
    global cnt
    Q.append(n)
    while Q:
        n = Q.pop(0)
        if n != k:
            for i in range(3):
                if i == 0:
                    nc = n - 1
                    if 0<=nc<=100000 and (con[nc] == 0 or con[nc] > con[n]+1):
                        Q.append(nc)
                        con[nc] = con[n] + 1
                elif i == 1:
                    nc = n + 1
                    if 0<=nc<=100000 and (con[nc] == 0 or con[nc] > con[n]+1):
                        Q.append(nc)
                        con[nc] = con[n] + 1
                else:
                    if n < 100000:
                        nc = n*2
                        if 0 <= nc <=100000 and (con[nc] == 0 or con[nc] > con[n]+1):
                            Q.append(nc)
                            con[nc] = con[n] + 1
        else:
            cnt = con[k]
            break

N, K = map(int,input().split())
con = [0]*100001
Q = []
cnt = 0
bfs(N,K)
print(cnt)