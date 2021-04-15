import sys
input = sys.stdin.readline

def perm(cnt,people,N):
    global M,arr,result
    if cnt >= N:
        people = people[:3]+[0]+people[3:]
        score  = 0
        player = 0
        for i in range(M):
            out = 0
            b1,b2,b3 = 0,0,0
            while out < 3:
                if arr[i][people[player]] == 0:
                    out += 1
                elif arr[i][people[player]] == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif arr[i][people[player]] == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif arr[i][people[player]] == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else:
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0
                player = (player + 1) % 9
        result = max(score ,result)
        return
    for i in range(cnt,N):
        people[i],people[cnt] = people[cnt],people[i]
        perm(cnt+1,people,N)
        people[i],people[cnt] = people[cnt],people[i]
M = int(input())
arr = [list(map(int,input().split())) for _ in range(M)]
result = -1
people = [1,2,3,4,5,6,7,8]
perm(0,people,8)
print(result)