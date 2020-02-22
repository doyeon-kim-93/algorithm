N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []
visit = [0]*N

def start(k):
    if k == M:
        print(' '.join(map(str,result)))
        return
    else:
        for z in range(N):
            if visit[z] == 1: continue
            visit[z] = 1
            result.append(arr[z])
            start(k+1)
            result.pop()
            visit[z] = 0
start(0)