def check(k):
    global flag
    if k == 7:
        if sum(result) == 100:
            result.sort()
            for i in range(7):
                print(result[i])
            flag = True
            return
    else:
        for i in range(len(arr)):
            if visit[i] == 0 and arr[i] not in result and flag == False:
                visit[i] = 1
                result.append(arr[i])
                check(k+1)
                visit[i] = 0
                result.pop()



arr = [int(input()) for _ in range(9)]
visit = [0] * 9
result = []
flag = False
check(0)