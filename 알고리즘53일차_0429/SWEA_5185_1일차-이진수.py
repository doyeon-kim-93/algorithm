T = int(input())
for tc in range(1,T+1):
    n, a = input().split()
    N = int(n)
    A = int(a,16)
    k = format(A, 'b')
    if len(k) == 4*N:
        result = str(k)
    else:
        result = '0' + str(k)
    print('#{} {}'.format(tc,result))
