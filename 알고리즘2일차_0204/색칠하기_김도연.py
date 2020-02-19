T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0]*10 for _ in range(10)]
    for k in range(N):
        if nums[k][4] == 1:
            for i in range(nums[k][0], nums[k][2] +1):
                for j in range(nums[k][1], nums[k][3] +1):
                    arr[i][j] += 1

        else:
            for i in range(nums[k][0], nums[k][2] +1):
                for j in range(nums[k][1], nums[k][3] +1):
                    arr[i][j] += 2
    con = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                con +=1
    print('#{} {}'.format(tc,con))
