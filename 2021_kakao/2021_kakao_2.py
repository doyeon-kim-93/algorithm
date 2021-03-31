def check(oreder,num,visit,cnt,idx):
    global tmpA, tmpCnt
    if cnt == num:
        tmp = set()
        for i,val in enumerate(visit):
            if val == 1:
                tmp.add(oreder[i])
        if tmp in tmpA:
            tmpCnt[tmpA.index(tmp)] += 1
        else:
            tmpA += [tmp]
            tmpCnt += [1]
        # print(tmp,tmpA,tmpCnt)
        return
    if cnt > num:
        return
    if idx >= len(oreder):
        return
    visit[idx] = 1
    check(oreder, num, visit, cnt+1, idx+1)
    visit[idx] = 0
    check(oreder, num, visit, cnt, idx+1)

def solution(orders, course):
    global tmpA, tmpCnt
    answer = []
    for num in course:
        tmpA = []
        tmpCnt = []
        for order in orders:
            visit = [0] * len(order)
            check(order,num,visit,0,0)
        if tmpCnt:
            maxCnt = max(tmpCnt)
            if maxCnt >= 2:
                for i,val in enumerate(tmpCnt):
                    if val == maxCnt:
                        tmpVal = sorted(list(tmpA[i]))
                        value = ''.join(tmpVal)
                        answer += [value]
    answer.sort()
    return answer

tmpA = []
tmpCnt = []


print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))