N = int(input())
if N >2:
    arr = [0] * (N + 1)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    for i in range(3,N+1):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[N])
else:
    arr = [0] * (3)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    print(arr[N])