def start(k):
    if k == M:
        con = 0
        for i in range(len(result)):
            if 0<= i+1 <len(result):
                if result[i] < result[i+1]:
                    con += 1
        if con == k-1:
            print("{}".format(" ".join(result)))
            return
        else:
            return
    else:
        for z in range(N):
            if visit[z] == 1: continue
            visit[z] = 1
            result.append(arr[z])
            start(k+1)
            visit[z] = 0
            result.pop()
N, M = map(int,input().split())
arr = []
result = []
for i in range(1,N+1):
    arr.append(str(i))
visit = [0]*N
start(0)