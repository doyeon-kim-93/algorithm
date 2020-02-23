def start(k):
    if k == M:
        con = 0
        for z in range(M):
            if 0<= z+1 < M:
                if int(result[z]) > int(result[z+1]):
                    break
                else:
                    con += 1
        if con == M-1:
            print(' '.join(map(str,result)))
            return
        else:
            return
    else:
        for i in range(N):
            result.append(arr[i])
            start(k+1)
            result.pop()

N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
result = []
start(0)