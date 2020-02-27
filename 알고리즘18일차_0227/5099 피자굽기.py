T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    c = list(map(int,input().split()))
    C = []
    for i in range(M):
        C.append((i,c[i]))
    pizza = [1]*M
    Q = []
    while sum(pizza) != 1 :
        if sum(pizza) >= N:
            if len(Q)==N :
                bake = Q[0][1]// 2
                if bake > 0:
                    Q.append((Q[0][0], bake))
                    Q.pop(0)
                else:
                    pizza[Q[0][0]] = 0
                    Q.pop(0)
            else:
                Q.append(C[0])
                C.pop(0)

        else:
            bake = Q[0][1]// 2
            if bake > 0:
                Q.append((Q[0][0], bake))
                Q.pop(0)
            else:
                pizza[Q[0][0]] = 0
                Q.pop(0)
    print('#{} {}'.format(tc,Q[0][0]+1))