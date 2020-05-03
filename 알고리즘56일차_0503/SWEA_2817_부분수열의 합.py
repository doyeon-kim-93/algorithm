def chek(k):
    global result,value
    if k == N:
        if value == M:
            result += 1
        return
    else:
        chek(k+1)
        value += arr[k]
        chek(k+1)
        value -= arr[k]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    value = 0
    result = 0
    chek(0)
    print('#{} {}'.format(tc,result))