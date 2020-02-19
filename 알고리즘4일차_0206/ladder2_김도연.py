import sys
sys.stdin = open("input (12).txt", "r")


for tc in range(1,11):
    N = int(input())
    arr2 = [list(map(int,input().split())) for _ in range(100)]
    for j in range(100):
        if arr2[0][j] == 1:
            i = 1
            count_ = 1
            direc = 0
            while i < 99:
                if arr[i][j] == arr[i][0]:
                    if arr[i][j + 1] == 1:
                        direc = 1
                        break
                    else:
                        i += 1
                        count_ += 1
                elif arr[i][j] == arr[0][99]:
                    if arr[i][j - 1] == 1:
                        direc = -1
                        break
                    else:
                        i += 1
                        count_ += 1
                else:
                    if arr[i][j + 1] == 1:
                        direc = 1
                        break
                    elif arr[i][j - 1] == 1:
                        direc = -1
                        break
                    else:
                        i += 1
                        count_ += 1
                if direc == 1:
                    j += 1
                    count_ += 1
                    while 1:
                        if arr[i + 1][j] == 1:
                            direc = 0
                            break
                        else:
                            j += 1
                            count_ += 1
                if direc == -1:
                    j += 1
                    count_ += 1
                    while 1:
                        if arr[i + 1][j] == 1:
                            direc = 0
                            break
                        else:
                            j -= 1
                            count_ += 1
