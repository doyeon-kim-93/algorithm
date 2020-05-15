import sys

sys.stdin = open('../input.txt', 'r')
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def seven(people,SearchStart,som_cnt):
    global result,pick
    if people == 4 and som_cnt == 0:
        return
    if people == 5 and som_cnt == 1:
        return
    if people == 6 and som_cnt == 2:
        return
    if people == 7 and som_cnt >= 4:
        if link_chek(*make_visit(pick)):
            result += 1
        return
    for z in range(SearchStart,25):
        pick += [z]
        if som[z]:
            seven(people+1,z+1,som_cnt+1)
        else:
            seven(people+1,z+1,som_cnt)
        pick.pop()

def make_visit(lst):
    visit = [[0]*5 for _ in range(5)]
    r = 0
    c = 0
    for z in lst:
        r = z//5
        c = z%5
        visit[r][c] = 1
    return visit , (r,c)

def link_chek(visit_list,point):
    q = deque([])
    q += [point]
    cnt = 1
    visited = [[0]*5 for _ in range(5)]
    visited[point[0]][point[1]] = 1
    while q :
        r,c = q.popleft()
        for t in range(4):
            nr = r + dr[t]
            nc = c + dc[t]
            if 0<=nr<5 and 0<=nc<5 and visited[nr][nc] == 0 and visit_list[nr][nc]:
                cnt += 1
                q += [(nr,nc)]
                visited[nr][nc] =1

    if cnt == 7:
        return True
    else:
        return False

arr = [list(input()) for _ in range(5)]
som = [0] * 25
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            som[i*5+j] = 1
pick = []
result = 0
seven(0,0,0)
print(result)
