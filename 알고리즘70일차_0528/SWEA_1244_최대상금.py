T = int(input())
for tc in range(1,T+1):
    strnum,strcount = input().split()
    numLi = []
    n = len(strnum)
    num = int(strnum)
    count = int(strcount)
    for i in range(n):
        one = num%10
        two = num//10
        num = two
        numLi.insert(0,one)
    t = 0
    flag = False
    com = []
    while count:
        if t == n-1:
            break
        else:
            for z in range(t+1,n):
                if numLi[t] < numLi[z]:
                    flag = True
                    break
            if flag:
                max_point = numLi[t]
                idx = t
                for j in range(t+1,n):
                    if max_point < numLi[j]:
                        max_point = numLi[j]
                        idx = j
                    elif max_point == numLi[j]:
                        idx = max(t,j)
                if t != idx:
                    numLi[t],numLi[idx] = numLi[idx],numLi[t]
                    count -= 1
                    if numLi.count(numLi[t])>1:
                        com.append(idx)
                t +=1
            else:
                t +=1
    for z in range(len(com)-1):
        if numLi[com[z]]>numLi[com[z+1]]:
            numLi[com[z]],numLi[com[z + 1]] = numLi[com[z + 1]],numLi[com[z]]
    if count:
        flag=True
        for i in numLi:
            if numLi.count(i) >= 2:
                flag=False
                break
        while count>0:
            if flag:
                numLi[-1], numLi[-2] = numLi[-2], numLi[-1]
                count -= 1
            else:
                break
    print('#{}'.format(tc),end=' ')
    print(''.join(map(str,numLi)))