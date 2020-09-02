import sys
sys.stdin = open("input.txt", "r")
from sys import stdin
input = stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs():
    global q
    flag2 = False
    while q:
        r,c = q.pop(0)
        flag = False
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<16 and 0<=nc<16 and visit[nr][nc] == 0:
                if arr[nr][nc] == "0":
                    visit[nr][nc] = 1
                    q += [(nr,nc)]
                elif arr[nr][nc] == "3":
                    flag = True
                    break
        if flag:
            flag2 = True
            break
    if flag2:
        return 1
    else:
        return 0


for _ in range(10):
    N = int(input())
    arr = list(list(input()) for _ in range(16))
    q = [(1,1)]
    visit = list([0]*16 for _ in range(16))
    visit[1][1] = 1
    print("#{} {}".format(N,bfs()))