T = int(input())
for tc in range(1,T+1):
    visit1 = [0] * 401
    N = int(input())
    for _ in range(N):
        r, c = map(int,input().split())
        if r < c:
            x = r
            y = c
            if x % 2 == 0 and y%2 != 0:
                x = x - 1
                y = y + 1
            for t in range(x,y+1):
                visit1[t] += 1

        else:
            x = c
            y = r
            if x % 2 == 0 and y%2 != 0:
                x = x - 1
                y = y + 1
            for t in range(x,y+1):
                visit1[t] += 1
    result = max(visit1)
    print("#{} {}".format(tc,result))