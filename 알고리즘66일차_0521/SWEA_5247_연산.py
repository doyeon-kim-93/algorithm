import collections

arr = [0,1,2,3]

def chek():
    global result,q
    while q:
        a,b = q.popleft()
        if a == M:
            result = min(result, b)
        for i in range(4):
            c = a
            d = b
            if i == 0:
                c += 1
                d += 1
                if 0 < c <= 1000000 and d < result and num[c] != 1:
                    q += [(c, d)]
                    num[c] = 1
            elif i == 1:
                c -= 1
                d += 1
                if 0 < c <= 1000000 and d < result and num[c] != 1:
                    q += [(c, d)]
                    num[c] = 1
            elif i == 2:
                c *= 2
                d += 1
                if 0 < c <= 1000000 and d < result and num[c] != 1:
                    q += [(c, d)]
                    num[c] = 1
            elif i == 3:
                c -= 10
                d += 1
                if 0 < c <= 1000000 and d < result and num[c] != 1:
                    q += [(c, d)]
                    num[c] = 1
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    result = 987654321
    num = [0] * 1000001
    q = collections.deque([])
    q += [(N,0)]
    chek()
    print('#{} {}'.format(tc,result))
