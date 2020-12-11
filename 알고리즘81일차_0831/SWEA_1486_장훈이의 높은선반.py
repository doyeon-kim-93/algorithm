def check(k,r):
    global N,B,result
    if k >= N:
        return
    if r >= result:
        return
    if r >= B :
        result = min(result,r)
        return
    else:
        for i in range(k,N):
            if visit[i] == 0:
                visit[i] = 1
                check(i,r+arr[i])
                visit[i] = 0

T = int(input())
for tc in range(1,T+1):
    N,B = map(int, input().split())
    arr = list(map(int,input().split()))
    visit = [0]*N
    result = 987654321
    check(0,0)
    print("#{} {}".format(tc,result-B))


def check(k,r):
    global N,B,result
    if k > N:
        return
    if r >= result:
        return
    if r >= B :
        result = min(result,r)
        return
    else:
        if k < N:
            check(k+1,r)
            check(k+1,r+arr[k])

T = int(input())
for tc in range(1,T+1):
    N,B = map(int, input().split())
    arr = list(map(int,input().split()))
    result = 987654321
    check(0,0)
    print("#{} {}".format(tc,result-B))
