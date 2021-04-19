def cicle(n,d,k):
    global arr
    tmpList = arr[n][:]
    if tmpList:
        L = len(tmpList)
        if d == 0:
            for i in range(L):
                idx = (i+k)%L
                arr[n][idx] = tmpList[i]
        else:
            for j in range(L):
                v = (j-k)
                if v >= 0:
                    v = v % L
                else:
                    v = L + v
                arr[n][v] = tmpList[j]
        return

def check(N,M):
    global arr, result
    conSum = 0
    conlen = 0
    tmp = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                conlen += 1
                conSum += arr[i][j]
                if j == 0:
                    if arr[i][j] == arr[i][1] and arr[i][j] != 0:
                        tmp += [(i,j),(i,1)]
                    if arr[i][j] == arr[i][M-1] and arr[i][j] != 0:
                        tmp += [(i, j), (i, M-1)]
                elif j == M-1:
                    if arr[i][j] == arr[i][0] and arr[i][j] != 0:
                        tmp += [(i,j),(i,0)]
                    if arr[i][j] == arr[i][M-2] and arr[i][j] != 0:
                        tmp += [(i, j), (i, M-2)]
                elif 1<= j <= M-2:
                    if arr[i][j] == arr[i][j-1] and arr[i][j] != 0:
                        tmp += [(i,j),(i,j-1)]
                    if arr[i][j] == arr[i][j+1] and arr[i][j] != 0:
                        tmp += [(i, j), (i, j+1)]
                if i == 0:
                    if arr[i][j] == arr[1][j] and arr[i][j] != 0:
                        tmp += [(i, j), (1, j)]
                elif i == N-1:
                    if arr[i][j] == arr[N-2][j] and arr[i][j] != 0:
                        tmp += [(i,j), (N-2,j)]
                elif 1 <= i <= N-2:
                    if arr[i][j] == arr[i-1][j] and arr[i][j] != 0:
                        tmp += [(i,j),(i-1,j)]
                    if arr[i][j] == arr[i+1][j] and arr[i][j] != 0:
                        tmp += [(i,j),(i+1,j)]
    tmp2 = set(tmp)
    tmp = list(tmp2)
    if tmp:
        for i,j in tmp:
            result -= arr[i][j]
            arr[i][j] = 0
    else:
        if conlen != 0:
            val = conSum/conlen
            for i in range(N):
                for j in range(M):
                    if arr[i][j] != 0:
                        if arr[i][j] > val:
                            arr[i][j] -= 1
                            result -= 1
                        elif arr[i][j] < val:
                            arr[i][j] += 1
                            result += 1

N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cicleList = [list(map(int,input().split())) for _ in range(T)]
result = 0
for i in range(N):
    result += sum(arr[i])
for t in range(T):
    n,d,k = cicleList[t][0],cicleList[t][1],cicleList[t][2]
    for j in range(1,N+1):
        if n != 0:
            if j % n == 0:
                cicle(j-1,d,k)
    check(N,M)
print(result)