import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    e = float(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1,N):
            arr[i][j]= arr[j][i] = ((x[i]-x[j])**2)+((y[i]-y[j])**2)
    INF = float('inf')
    key = [INF] * N
    visit = [0] * N
    key[0] = 0
    cnt = 0
    result = 0
    while cnt < N:
        U = -1
        minValue = INF
        for i in range(N):
            print(key[i])
            if not visit[i] and key[i] < minValue:
                minValue = key[i]
                U = i
        visit[U] = 1
        result += minValue
        cnt += 1
        for z in range(N):
            if not visit[z] and key[z]> arr[U][z]:
                key[z] = arr[U][z]
    print('#{} {}'.format(tc,int(round(e*result))))