T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    check = [0] * N
    B = list(map(int,input().split()))
    for j in range(M):
        for z in range(N):
            if B[j] >= A[z]:
                check[z] += 1
                break
    result = check.index(max(check))
    print('#{} {}'.format(tc,result+1))

