T = int(input())
for tc in range(1,T+1):
    M = input()
    N = input()
    m = {}
    for i in range(len(M)):
        m[M[i]] = 0
    for key in m.keys() :
        for j in range(len(N)):
            if key == N[j]:
                m[key] += 1
    max_num = 0
    for i in m.values():
        if i > max_num:
            max_num = i
    print('#{} {}'.format(tc,max_num))

