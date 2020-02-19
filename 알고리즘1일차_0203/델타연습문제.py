# k=5
# m=5
# arr=[list([0]*m) for _ in range(k)]
#
# num=1
# for i in range(k):
#     for j in range(m):
#         arr[i][j] = num
#         num += 1
#
# dc = [-1,1,0,0]
# dr = [0,0,1,-1]

#1. 1부터 25까지 증가하면서 5 5 크기의 배열에 입력
arr = [[0] *5 for _ in range(5)]
num=1
for i in range(5):
    for j in range(5):
        arr[i][j] = num
        num += 1
print(arr)
#2  2.이웃한 요소가 홀수일때만 더한 값을 출력하기
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for i in range(5):
    for j in range(5):
        sum = 0
        for k in range(4):
            nr = i +dr[k]
            nc = j +dc[k]
            if nr >= 0 and nr <5 and nc >=0 and nc <5:
                if arr[nr][nc] %2 != 0:
                    sum += arr[nr][nc]
        print(sum)

#3 이웃한 요소 절대값 차의 합을 구하기
def m_abs(num):
    if num < 0:
        return -num
    return num
for i in range(5):
    for j in range(5):
        sum = 0
        for k in range(4):
            nr = i +dr[k]
            nc = j +dc[k]
            if nr >= 0 and nr <5 and nc >=0 and nc <5:
                if arr[nr][nc] %2 != 0:
                    sum += m_abs(arr[nr][nc] - arr[i][j])
        print(sum)

#4 상하좌우를 제외한 대각 요소 접근해 합을 구하고 그 합 중 가장 큰 값을 출력
dr2 = [-1,-1,1,1]
dc2 = [-1,1,-1,1]
max_value=0
for i in range(5):
    for i in range(5):
        sum = 0
        for k in range(4):
            nr = i + dr2[k]
            nc = j + dc2[k]
            if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
                if arr[nr][nc] % 2 != 0:
                    sum += arr[nr][nc]
        if sum > max_value:
            max_value = sum
print(max_value)

