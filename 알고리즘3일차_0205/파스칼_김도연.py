T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr =[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j == 0:
                arr[i][j] = 1
            if i == j:
               arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(arr)