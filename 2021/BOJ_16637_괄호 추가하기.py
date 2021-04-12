def check(i,M,visit):
    global arr,confirm,result
    if i >= M :
        numList = []
        calList = []
        flag = True
        idx = 0
        for j,val in enumerate(arr):
            if val in confirm:
                if visit[idx] == 1:
                    preNum = numList.pop()
                    flag = False
                    if val == '*':
                        preNum *= int(arr[j+1])
                    elif val == "+":
                        preNum += int(arr[j + 1])
                    elif val == "-":
                        preNum -= int(arr[j + 1])
                    numList += [preNum]
                else:
                    calList += [val]
                idx += 1
            else:
                if flag:
                    numList += [int(val)]
                else:
                    flag = True
        num = numList.pop(0)
        while numList:
            cal = calList.pop(0)
            num2 = numList.pop(0)
            if cal == '*':
                num *= num2
            elif cal == "+":
                num += num2
            elif cal == "-":
                num -= num2
        result = max(result,num)
        return
    visit[i] = 1
    check(i+2,M,visit)
    visit[i] = 0
    check(i+1, M, visit)

N = int(input())
arr = input()
confirm = ['*','+','-']
cal = []
for i in arr:
    if i in confirm:
        cal += [i]
visit = [0] * len(cal)
result = (-2)**(31)
check(0,len(cal),visit)
print(result)