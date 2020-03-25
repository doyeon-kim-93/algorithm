import copy
def filter(k,start,t):
    global chk, eli, pick, lens
    if k == t :
        a = copy.deepcopy(pick)
        eli += [a]
        return
    else:
        for z in range(start,lens):
            pick += [chk[z]]
            filter(k+1,z+1,t)
            pick.pop()
N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
chk = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home += [(i,j)]
        elif city[i][j] == 2:
            chk += [(i,j)]
# print(chk)
# print(home)
lens = len(chk)
eli = []
pick = []
for x in range(1,M+1):
    filter(0,0,x)
# print(eli)
# print(len(eli))
result = 987654321
for i in range(len(eli)):
    line_sum = 0
    for j in range(len(home)):
        home_one = 987654321
        for x in range(len(eli[i])):
            line = abs(eli[i][x][0]-home[j][0]) + abs(eli[i][x][1]-home[j][1])
            home_one = min(home_one,line)
        line_sum += home_one
    result = min(result,line_sum)
print(result)
