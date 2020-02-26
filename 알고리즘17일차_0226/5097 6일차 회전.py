def rotation(k,K):
    if k == K:
        print("#{} {}".format(tc,num[0]))
        return
    else:
        num.extend([num.pop(0)])
        rotation(k+1,K)
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    num = list(map(int,input().split()))
    rotation(0,M)