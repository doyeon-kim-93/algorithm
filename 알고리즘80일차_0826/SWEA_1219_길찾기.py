import sys
sys.stdin = open("input.txt", "r")
from sys import stdin
input = stdin.readline

def dfs(k):
    global result
    if k == 99:
        result = 1
        return
    else:
        if len(route[k]) == 0:
            return
        else:
            for z in range(len(route[k])):
                dfs(route[k][z])

for _ in range(10):
    t,n = map(int,input().split())
    arr = list(map(int,input().split()))
    route = [[] for _ in range(100)]
    for i in range(0,len(arr),2):
        route[arr[i]].append(arr[i+1])
    visit = [[0] for _ in range(100)]
    result = 0
    dfs(0)
    print("#{} {}".format(t,result))