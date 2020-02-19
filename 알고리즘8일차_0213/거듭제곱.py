def power(N,n):
    if n == 1:
        return N
    return power(N,n-1) * N
tc = int(input())
N, n = map(int,input().split())
print('#{} {}'.format(tc,power(N,n)))