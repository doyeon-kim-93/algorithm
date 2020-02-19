R,C= map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(R)]



for i in range(R):
    if i%2:
        for j in range(C):
            print(arr[i][j], end=' ')

    else:
        for j in range(C - 1, -1, -1):
            print(arr[i][j], end=' ')

# for i in range(R):
#     for j in range(C):
#         print(arr[i][j+(C-1-2*j)*(i%2)], end = ' ')