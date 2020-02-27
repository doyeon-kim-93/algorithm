def check(k):
    global calc, max_, min_
    if k == len(ope):
        for i in range(k):
            if i == 0:
                if table[i] == '+':
                    calc = num[0] + num[1]
                elif table[i] == '-':
                    calc = num[0] - num[1]
                elif table[i] == '*':
                    calc = num[0] * num[1]
                elif table[i] == '/':
                    calc = int(num[0] / num[1])
            else:
                if table[i] == '+':
                    calc += num[i+1]
                elif table[i] == '-':
                    calc -= num[i+1]
                elif table[i] == '*':
                    calc *= num[i+1]
                elif table[i] == '/':
                    calc = int(calc /num[i+1])
        if calc > max_:
            max_ = calc
        if calc < min_:
            min_ = calc
        return
    else:
        che = 0
        for i in range(len(ope)):
            if ope_visit[i] == 0 and che != ope[i] :
                ope_visit[i] = 1
                che = ope[i]
                table.append(ope[i])
                check(k+1)
                table.pop()
                ope_visit[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    op = ['+', '-', '*', '/']
    ope_cnt = list(map(int,input().split()))
    num = list(map(int, input().split()))
    ope =[]
    for i in range(4):
        if ope_cnt[i] != 0:
            for _ in range(ope_cnt[i]):
                ope.append(op[i])
    ope_visit = [0] * len(ope)
    table = []
    max_ = -12345678
    min_ = 123456789
    calc = 0
    result = []
    check(0)
    print('#{} {}'.format(tc,max_- min_))

