def perm(idx,N,arr):
    global re
    if idx >= N:
        tmp = ''
        for i in range(len(arr)):
            tmp += arr[i]
        # print(tmp)
        re.add(int(tmp))
        return
    for i in range(idx,N):
        arr[i], arr[idx] =  arr[idx], arr[i]
        perm(idx+1,N,arr)
        arr[i], arr[idx] = arr[idx], arr[i]

def check(k,N,array,visit):
    if k == N:
        numberlist = []
        for i in range(len(visit)):
            if visit[i]:
                numberlist += array[i]
        if numberlist:
            # print(numberlist,"*************")
            perm(0,len(numberlist),numberlist)
        return
    visit[k] = 1
    check(k+1,N,array,visit)
    visit[k] = 0
    check(k+1,N,array,visit)
def solution(numbers):
    global re
    re = set()
    arr = []
    for i in range(len(numbers)):
        arr += [numbers[i:i+1]]
    visited = [0] * len(arr)
    check(0, len(arr), arr, visited)
    result = list(re)
    result.sort()
    resultCnt = 0
    for i in range(len(result)):
        num = int(result[i])
        if num == 1 or num == 0:
            continue
        # print(num)
        cnt = 0
        for j in range(1,num):
            if num % j == 0:
                cnt += 1
            if cnt >= 2:
                break
        if cnt == 1:
            resultCnt += 1
    # print(re,"#############")
    return resultCnt
re = set()

print(solution("17"))
print(solution("011"))
