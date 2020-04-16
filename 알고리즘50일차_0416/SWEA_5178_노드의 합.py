T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    node = [0]*(N+1)
    for i in range(M):
        a,b = map(int,input().split())
        node[a] = b
    for i in range(N,-1,-1):
        if node[i] == 0 and i != 0:
            if 0<(2*i)<N+1 and  0<(2*i)+1<N+1:
                node[i] = node[2*i]+node[(2*i)+1]
            elif 0<(2*i)<N+1:
                node[i] = node[2 * i]
    print('#{} {}'.format(tc,node[L]))