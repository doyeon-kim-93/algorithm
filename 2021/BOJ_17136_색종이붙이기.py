def check(r,c,cnt):
    global reuslt,paper,arr
    if c >= 10:
        reuslt = min(reuslt,cnt)
        return
    if r >= 10:
        check(0,c+1,cnt)
        return
    if cnt >= reuslt:
        return
    if arr[r][c] == 1:
        for z in range(5):
            if paper[z] == 0:
                continue
            if r+z >= 10 or c+z >= 10:
                continue
            flag = True
            for i in range(r,r+z+1):
                for j in range(c,c+z+1):
                    if arr[i][j] == 0 :
                        flag = False
                        break
                if not flag:
                    break

            if flag:
                for i in range(r, r + z + 1):
                    for j in range(c, c + z + 1):
                        arr[i][j] = 0
                paper[z] -= 1
                check(r+z+1,c,cnt+1)
                paper[z] += 1
                for i in range(r, r + z + 1):
                    for j in range(c, c + z + 1):
                        arr[i][j] = 1
    else:
        check(r+1,c,cnt)

arr = [list(map(int,input().split())) for _ in range(10)]
paper = [5,5,5,5,5]
reuslt = 987654321
check(0,0,0)
if reuslt == 987654321:
    print(-1)
else:
    print(reuslt)
