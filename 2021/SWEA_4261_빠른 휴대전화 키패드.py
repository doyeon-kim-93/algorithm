def keyboard(a):
    if a == '2':
        return ['a', 'b', 'c']
    elif a == '3':
        return ['d', 'e', 'f']
    elif a == '4':
        return ['g', 'h', 'i']
    elif a == '5':
        return ['j', 'k', 'l']
    elif a == '6':
        return ['m', 'n', 'o']
    elif a == '7':
        return ['p', 'q', 'r', 's']
    elif a == '8':
        return ['t', 'u', 'v']
    elif a == '9':
        return ['w', 'x', 'y', 'z']


T = int(input())

for tc in range(1, T + 1):
    S, N = input().split()
    result = 0
    N = int(N)
    d = list(map(str, input().split()))
    for k in range(N):
        con = 0
        if len(S) != len(d[k]):
            continue
        for j in range(len(d[k])):
            if d[k][j] in keyboard(S[j]):
                con = con + 1
        if con == len(d[k]):
            result = result + 1
    print("#{} {}".format(tc,result))