T = int(input())
for tc in range(1,T+1):
    W, H, N = map(int,input().split())
    point = []
    result = 0
    for _ in range(N):
        i,j = map(int,input().split())
        point += [[i,j]]
    for i in range(N-1):
        r = point[i+1][0] - point[i][0]
        c = point[i+1][1] - point[i][1]
        if r*c < 0:
            result += abs(r)
            result += abs(c)
        else:
            result += max(abs(r),abs(c))
    print("#{} {}".format(tc, result))

