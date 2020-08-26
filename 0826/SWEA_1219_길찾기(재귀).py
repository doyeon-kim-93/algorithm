import sys
sys.stdin = open("input.txt", "r")
from sys import stdin
input = stdin.readline

#길이 있는지 없는지 판단하는 문제는 BFS 가 DFS 보다 오래 걸리는 경우도 있음 따라서 DFS 풀어봅시다!

def dfs(v): #경로 찾기, 경로를 찾으면 1, 못찾으면 0
    global adj,N,visited
    # 기저영역 : 더이상 재귀가 호출되지 않는 영역
    # 목적지에 다달았거나, 이미 방문한 지점일 경우 더이상 실행하지 않음
    if v == 99:
        return 1
    if visited[v] == 1:
        return 0

    visited[v] = 1 # 해당 지점을 방문했음을 표시

    # 실행영역 : 연산을 실행하는 부분(재귀 호출 실행)
    # 현재 지점에서 도착할 수있는 모든 지점에 대해서 진행
    result1 = 0
    result2 = 0
    if adj[0][v] != 0:
        result1 = dfs(adj[0][v])
    if adj[1][v] != 0:
        result2 = dfs(adj[1][v])

    return result1 or result2


T = 10
for _ in range(T):
    tc, N = map(int,input().split())
    result = 0
    path = list(map(int,input().split()))
    # 그래프 탐색할 때는 그래프의 노드간 연결정보를 알아야함
    # 보통 인접행렬이나 인접리스트를 통해서 표현한다.
    adj = [[0] * 100 for _ in range(2)]
    visited = [0] * 100
    # 인접행렬에 지점간 연결정보 넣기
    #  0  1  2  3
    # [3][ ][ ][ ]
    # [ ][ ][ ][ ]
    for i in range(0,len(path),2):
        if adj[0][path[i]] == 0:
            adj[0][path[i]] = path[i+1]
        else:
            adj[1][path[i]] = path[i+1]
    # 인접행렬 이용해서 그래프 순회
    result = dfs(0)
    print("#{} {}".format(tc,result))