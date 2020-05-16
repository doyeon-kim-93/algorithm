def chek():
    global cnt,result
    result = max(result,cnt)
    for r in range(0,N,2):
        for c in range(N):
            if arr[r][c] == 1 and UpAngle[r+c] == 0 and DownAngle[N-(r-c)-1] == 0:
                arr[r][c] = 2
                UpAngle[r+c] = 1
                DownAngle[N-(r-c)-1] = 1
                cnt += 1
                chek()
                UpAngle[r+c] = 0
                DownAngle[N-(r-c)-1] = 0
                cnt -= 1
                arr[r][c] = 1
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
UpAngle = [0]*((2*N)-1)
DownAngle = [0]*((2*N)-1)
cnt = 0
result = -1
chek()
print(result)
