N = 10

memo = [0,1]
def fibo_py(N):
    if N >=2 and len(memo) <= N :
        memo.append(fibo_py(N-1)+fibo_py(N-2))
    return memo[N]

print(fibo_py(N))
print(memo)

memo2 = [-1] * (N+1)
memo2[0] = 0
memo2[1] = 1
def fibo(N):
    if memo2[N] == -1:
        memo2[N] = fibo(N-1) + fibo(N-2)
    return memo2[N]

print(fibo(N))
print(memo2)
