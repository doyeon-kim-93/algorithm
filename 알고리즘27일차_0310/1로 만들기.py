def check(k,t):
    global result
    if t >= result:
        return
    if k == 1:
        result = min(result,t)
        return
    else:
        if k%3 == 0:
            check(int(k//3),t+1)
        if k%2 == 0:
            check(int(k//2),t+1)
        check(k-1,t+1)

N = int(input())
result = 123456789
check(N,0)
print(result)
