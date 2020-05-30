import math

def chek(number):
    if len(number) == N:
        flag = True
        for i in range(2,int(math.sqrt(int(number)))+1):
            if int(number)%i == 0:
                flag = False
                break
        if flag:
            print(number)
        else:
            return
    else:
        for i in range(2,int(math.sqrt(int(number)))+1):
            if int(number)%i == 0:
                return
    for z in num:
        chek(number+z)




N = int(input())
start = ['2','3','5','7']
num = ['1','3','7','9']
for x in start:
    chek(x)