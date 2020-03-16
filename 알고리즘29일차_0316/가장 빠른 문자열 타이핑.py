T = int(input())
for tc in range(1,T+1):
    A, B = map(str,input().split())
    N = len(A)
    M = len(B)
    C,D = A,B
    con = []
    for i in range(N):
        T = C.find(D)
        if T >= 0:
            con += [C.find(D)]
            C = C[con[i]+M:]
    che = len(con)
    print('#{} {}'.format(tc,N-(M*che)+che))