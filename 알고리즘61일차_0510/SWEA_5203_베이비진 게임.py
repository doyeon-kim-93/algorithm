def chek1():
    global flag,flag3,result1,result2
    con1 = 0
    con2  = 0
    for i in range(10):
        if p1[i] >=3:
            con1 = 1
        elif p2[i] >=3:
            con2 = 1
    if con1 > 0 or con2 > 0:
        flag = 1
        flag3 = 1
        if con1 > con2 :
            result1 = 1
        elif con2 > con1:
            result2 = 1

def chek2():
    global flag, result1, result2
    con1 = 0
    con2 = 0
    i = 0
    flag2 = 0
    while i < 8:
        cnt1 = 0
        cnt2 = 0
        for z in range(i,i+3):
            if p1[z] > 0:
                cnt1 += 1
            if p2[z] > 0:
                cnt2 += 1
        if cnt1 == 3 or cnt2 == 3:
            flag = 1
            if cnt1 == 3:
                con1 = 1
            if cnt2 == 3:
                con2 = 1
        i += 1
        if flag:
            flag2 = 1
        if flag2:
            break
    if con1 > con2:
        result1 = 1
    elif con1 < con2:
        result2 = 1

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    result = 0
    result1 = 0
    result2 = 0
    flag = 0
    flag3 = 0
    flag4 = 0
    for z in range(6):
        if z > 3:
            chek1()
            chek2()
            if not flag:
                p1[arr[z * 2]] += 1
                p2[arr[(z * 2) + 1]] += 1
            else:
                break
        else:
            p1[arr[z*2]] += 1
            p2[arr[(z*2)+1]] += 1

        if flag:
            break
    if result1 > result2:
        result = 1
    elif result1 < result2:
        result = 2
    print(result)