T = int(input())
for tc in range(1,T+1):
    arr = list(input())
    N = len(arr)
    che = [0] * len(arr)
    box = []
    point = 0
    for i in range(N):
        if arr[i] == '(':
            box += [point]
            che[i] = point
            point += 1
        else:
            che[i] = box.pop()
    for i in range(N):
        if 0<i+1<len(che):
            if che[i] == che[i+1]:
                che[i],che[i+1] = '*',' '
    cnt = 0
    for z in range(N):
        if type(che[z]) == int:
            start = che[z]
            cnt += 1
            while 1:
                z += 1
                if che[z] == start:
                    che[z] = ''
                    break
                elif che[z] == '*':
                    cnt += 1
    print("#{} {}".format(tc,cnt))