def check(cnt,cost):
    global result,N,arr
    if cnt >= N:
        result = max(result,cost)
        return
    if (cnt+arr[cnt][0]-1) < N:
        check(cnt+arr[cnt][0],cost+arr[cnt][1])
    check(cnt + 1, cost)
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = -1
check(0,0)
print(result)