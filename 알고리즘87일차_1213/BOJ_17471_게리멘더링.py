import collections

def conect(arr2):
    global q, board
    visit = [0] * (N+1)
    q += [arr2[0]]
    visit[arr2[0]] = 1
    while q:
        idx = q.popleft()
        for i in range(1,N+1):
            if board[idx][i] == 1 and visit[i] == 0 and i in arr2:
                visit[i] = 1
                q += [i]
    if sum(visit) == len(arr2):
        return True
    else:
        return False

def divide(arr):
    G1 = []
    G2 = []
    for i in range(1,N+1):
        if arr[i]:
            G1 += [i]
        else:
            G2 += [i]
    if conect(G1) and conect(G2):
        return True
    else:
        return False
    # print('-------------')
    # print(G1)
    # print(G2)

def check(idx,cnt,k):
    global selec,resultBol,point,result
    if cnt == k:
        if divide(selec):
            resultBol = True
            G1 = 0
            G2 = 0
            for i in range(1,N+1):
                if selec[i]:
                    G1 += point[i]
                else:
                    G2 += point[i]
            result = min(result,abs(G1-G2))
        return

    if idx >= N+1:
        return
    selec[idx] = 1
    check(idx+1,cnt+1,k)
    selec[idx] = 0
    check(idx+1,cnt,k)

N = int(input())
point = [0] + list(map(int,input().split()))
board = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    info = list(map(int,input().split()))
    for j in range(1,info[0]+1):
        board[i][info[j]] = board[info[j]][i] = 1
selec = [0] * (N+1)
q = collections.deque([])
result = 987654321
resultBol = False
for i in range(1,(N//2)+1):
    check(1,0,i)
if resultBol:
    print(result)
else:
    print(-1)
