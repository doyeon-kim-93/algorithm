def dircheck(k,dir):
    dirList = [(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]
    if k == 'U':
        if dir == 'L':
            return dirList[2]
        else:
            return dirList[3]
    elif k == 'D':
        if dir == 'L':
            return dirList[3]
        else:
            return dirList[2]
    elif k == 'R':
        if dir == 'L':
            return dirList[0]
        else:
            return dirList[1]
    elif k == 'L':
        if dir == 'L':
            return dirList[1]
        else:
            return dirList[0]

N = int(input())
appleCnt = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(appleCnt):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 2
dirCnt = int(input())
dirList = []
timeList = []
for _ in range(dirCnt):
    time,Dir = input().split()
    dirList += [(int(time),Dir)]
    timeList += [int(time)]
presentSec = 0
snack = [[0]*N for _ in range(N)]
snack[0][0] = 1
snackPosition = [(0,0)]
Dir = 'R'
dr,dc = 0,1
headR,headC = 0,0
while 1:
    presentSec += 1
    headR += dr
    headC += dc
    if headR<0 or headR>=N or headC<0 or headC>=N:
        break
    else:
        if snack[headR][headC] == 1:
            break
        else:
            snack[headR][headC] = 1
            snackPosition += [(headR,headC)]
            if arr[headR][headC] == 2:
                arr[headR][headC] = 0
            elif arr[headR][headC] != 2:
                tailR,tailC = snackPosition[0]
                snack[tailR][tailC] = 0
                snackPosition.pop(0)
            if timeList:
                if presentSec == timeList[0]:
                    dr,dc,Dir = dircheck(Dir,dirList[0][1])
                    timeList.pop(0)
                    dirList.pop(0)
print(presentSec)



