import sys
sys.stdin = open("input.txt", "r")
from sys import stdin
input = stdin.readline

def bfs(e,idx,cnt):
    global result,N
    print(idx,cnt,N)
    if idx == N:
        result = min(result,cnt)
        return
    elif cnt >= result:
        return
    else:
        bfs(arr[idx],idx+1,cnt+1)
        e-=1
        if e > 0:
            bfs(e,idx+1,cnt)


T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))+[0]
    N = arr[0]
    result = 987654321
    bfs(arr[1],2,0)
    print("#{} {}".format(tc,result))