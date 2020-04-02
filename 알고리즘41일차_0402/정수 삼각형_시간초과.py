N = int(input())
pira = [list(map(int,input().split())) for _ in range(N)]
result = -1
def check(line,point,con):
    global N, pira ,result
    if line == N:
        result = max(con,result)
        return
    else:
        check(line + 1, point + 1, con + pira[line][point + 1])
        check(line + 1, point, con + pira[line][point])
check(1,0,pira[0][0])
print(result)
