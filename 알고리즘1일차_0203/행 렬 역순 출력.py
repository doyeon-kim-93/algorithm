R,C= map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(R)]
# 행 역우선순회 방식 ver1
for i in range(R):
    for j in range(C-1,-1,-1):
        print(arr[i][j], end=' ')
    print()

print()
# 행 역우선순회 방식 ver2
for i in range(R):
    for j in range(C):
        print(arr[i][C-1-j], end=' ')
    print()

print('\b')
# 열 역우선순회 방식
for i in range(C):
    for j in range(1,R+1):
        print(arr[-j][i], end=' ')
