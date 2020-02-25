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

def key(k,start):
    if k == L:
        if check(result):
            print(''.join(result))
            return
    else:
        for i in range(start,C):
            result.append(number[i])
            key(k+1,i+1)
            result.pop()

L, C = map(int,input().split())
number = list(map(str, input().split()))
number.sort()
result = []
A = 'auieo'
key(0,0)