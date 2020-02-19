T=int(input())
for i in range(1,T+1):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    if m < n//k :
        print(f'#{i} {0}')
    con=0
    for j in range(len(arr)):
        if arr[j] != arr[-1]:
            if arr[j] + (k+1) > arr[j+1]:
                con += 1
    if con+1 == len(arr):
        result = n//k
        print(f'#{i} {result}')
    else:
        print(f'#{i} {0}')