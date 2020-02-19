T = int(input())
for v in range(1,T+1):
    N = int(input())
    nums = list(range(1,(N**2)+1))
    arr = [[0]*N for _ in range(N)]
    if N%2==0:
        M = N//2
    else:
        M = N//2+1
    for j in range(M):
        for i in range(j,N-j):
            if nums == []:
                break
            arr[N-N+j][i] = nums[0]
            nums.remove(nums[0])

        for i in range(1+j,N-j):
            if nums == []:
                break
            arr[i][N-1-j] = nums[0]
            nums.remove(nums[0])

        for i in range(N-2-j,-1+j,-1):
            if nums == []:
                break
            arr[N-1-j][i] = nums[0]
            nums.remove(nums[0])

        for i in range(N-2-j,0+j,-1):
            if nums == []:
                break
            arr[i][N-N+j] = nums[0]
            nums.remove(nums[0])

    print('#{}'.format(v))
    for i in range(N):
        print(" ".join(map(str, arr[i])))