def chek(k,con):
    global result,N,M
    if k == 3:
        if con < M+1:
            result = max(result,con)
    else:
        for z in range(N):
            if visit[z] == 0:
                con += arr[z]
                k += 1
                visit[z] = 1
                chek(k,con)
                con -=arr[z]
                k -= 1
                visit[z] =0

N,M = map(int,input().split())
arr = list(map(int,input().split()))
visit = [0]*N
result = 0
chek(0,0)
print(result)