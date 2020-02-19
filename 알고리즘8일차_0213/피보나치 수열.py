cnt = 0
def fibo(N):
    global cnt
    cnt += 1
    if 0< N < 3:
        return 1
    return fibo(N-1) + fibo(N-2)
print(fibo(10))
print(cnt)