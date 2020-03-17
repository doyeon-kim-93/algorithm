T = int(input())
for tc in range(1,T+1):
    arr = list(input())
    N = len(arr)
    stick = 0
    cnt = 0
    for i in range(N):
        if arr[i] == '(':
            stick += 1
        else:
            if 0<= i-1 < N:
                if arr[i-1] == '(':
                    stick -= 1
                    cnt += stick
                else:
                    stick -= 1
                    cnt += 1
    print("#{} {}".format(tc, cnt))


