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

    for