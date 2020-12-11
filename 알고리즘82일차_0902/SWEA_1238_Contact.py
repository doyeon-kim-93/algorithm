import sys
sys.stdin = open("input.txt", "r")
from sys import stdin
input = stdin.readline

def bfs():
    global q
    while q:
        k = q.pop(0)
        for z in range(101):
            if rearr[k][z] == 1 and visit[z] == 0:
                visit[z] = visit[k] + 1
                q += [z]
for tc in range(1,11):
    n,s = map(int,input().split())
    arr = list(map(int,input().split()))
    rearr = [[0]*101 for _ in range(101)]
    visit = [0]*101
    for i in range(0,n,2):
        rearr[arr[i]][arr[i+1]] = 1
    q = [s]
    visit[s] = 1
    bfs()
    maxnum = max(visit)
    result = 0
    for i in range(101):
        if visit[i] == maxnum:
            result = i
    print("#{} {}".format(tc,result))