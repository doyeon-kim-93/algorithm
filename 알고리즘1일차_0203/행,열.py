
R,C= map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(R)]
# 행 우선순회 방식\

for i in range(R):
    for j in range(C):
        print(arr[i][j], end=' ')

print('\b')
# 열 우선순회 방식
result = []
for i in range(C):
    for j in range(R):
        result.append(arr[j][i])
print(result)