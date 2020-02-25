def check(li):
    con_A = 0
    con_a = 0
    for i in range(L):
        if li[i] in A:
            con_A += 1
        else:
            con_a += 1
    if con_A >= 1 and con_a >= 2:
        return True
    else:
        return False

def key(k):
    if k == L:
        if check(result):
            flag = True
            for i in range(L):
                if 0 <= i+1 < L:
                    if result[i] >= result[i+1] :
                        flag = False
                        break
            if flag:
                print(''.join(result))
                return
    else:
        for i in range(C):
            if number[i] not in result :
                result.append(number[i])
                key(k+1)
                result.pop()

L, C = map(int,input().split())
number = list(map(str, input().split()))
number.sort()
result = []
A = 'auieo'
key(0)