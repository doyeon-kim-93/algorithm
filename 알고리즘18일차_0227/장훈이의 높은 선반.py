def check(s):
    global result
    if sum(High) >= B:
        if sum(High) < result:
            result = sum(High)
            return
    else:
        for i in range(s,len(H)):
            High.append(H[i])
            check(i+1)
            High.pop()

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    H = list(map(int,input().split()))
    High = []
    result = 12345678
    check(0)
    print('#{} {}'.format(tc,result-B))