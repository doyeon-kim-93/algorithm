def Bchek():
    global Bcnt,Bresult
    Bresult = max(Bresult,Bcnt)
    for r in range(N):
        if r%2 != 0:
            for c in range(0,N,2):
                if arr[r][c] == 1 and UpAngle[r+c] == 0 and DownAngle[N-(r-c)-1] == 0:
                    arr[r][c] = 2
                    UpAngle[r+c] = 1
                    DownAngle[N-(r-c)-1] = 1
                    Bcnt += 1
                    Bchek()
                    UpAngle[r+c] = 0
                    DownAngle[N-(r-c)-1] = 0
                    Bcnt -= 1
                    arr[r][c] = 1
        else:
            for c in range(1,N,2):
                if arr[r][c] == 1 and UpAngle[r+c] == 0 and DownAngle[N-(r-c)-1] == 0:
                    arr[r][c] = 2
                    UpAngle[r+c] = 1
                    DownAngle[N-(r-c)-1] = 1
                    Bcnt += 1
                    Bchek()
                    UpAngle[r+c] = 0
                    DownAngle[N-(r-c)-1] = 0
                    Bcnt -= 1
                    arr[r][c] = 1

def Wchek():
    global Wcnt,Wresult
    Wresult = max(Wresult,Wcnt)
    for r in range(N):
        if r&2 != 0:
            for c in range(1, N, 2):
                if arr[r][c] == 1 and UpAngle[r+c] == 0 and DownAngle[N-(r-c)-1] == 0:
                    arr[r][c] = 2
                    UpAngle[r+c] = 1
                    DownAngle[N-(r-c)-1] = 1
                    Wcnt += 1
                    Wchek()
                    UpAngle[r+c] = 0
                    DownAngle[N-(r-c)-1] = 0
                    Wcnt -= 1
                    arr[r][c] = 1
        else:
            for c in range(0, N, 2):
                if arr[r][c] == 1 and UpAngle[r+c] == 0 and DownAngle[N-(r-c)-1] == 0:
                    arr[r][c] = 2
                    UpAngle[r+c] = 1
                    DownAngle[N-(r-c)-1] = 1
                    Wcnt += 1
                    Wchek()
                    UpAngle[r+c] = 0
                    DownAngle[N-(r-c)-1] = 0
                    Wcnt -= 1
                    arr[r][c] = 1
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
UpAngle = [0]*((2*N)-1)
DownAngle = [0]*((2*N)-1)
Wcnt = 0
Bcnt = 0
Wresult = -1
Bresult = -1
Wchek()
Bchek()
print(Wresult+Bresult)
