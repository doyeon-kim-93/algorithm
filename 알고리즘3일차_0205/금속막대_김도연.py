import sys
sys.stdin = open("input (9).txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    base = list(map(int,input().split()))
    arr = [[0,0] for _ in range(N)]
    k=0

    for i in range(N):
        for j in range(2):
            arr[i][j] = base[k]
            k +=1
    arr2 = [[0, 0] for _ in range(N)]
    i = 0
    for j in range(N):
        if arr[i][1] == arr[j][0]:
            arr2[i],arr2[i+1] = arr[i],arr[j]
            i +=1
        # else:
        #     for j in range(N):
        #         if arr[i][1] == arr[j][0]:
        #             arr[i],arr[i + 1]

    print(arr2)
