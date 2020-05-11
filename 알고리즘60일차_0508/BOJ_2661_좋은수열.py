def back_tracking(idx):
    global result
    for i in range(1, (idx//2) + 1):
        if s[-i:] == s[-2*i:-i]:
            return -1

    if idx == n:
        for i in range(n):
            con = ''.join(map(str,s))
            result = min(result,int(con))
        return 0

    for i in range(1, 4):
        s.append(i)
        if back_tracking(idx + 1) == 0:
            return 0
        s.pop()

n = int(input())
s = []
result = 987654321
back_tracking(0)
print(result)