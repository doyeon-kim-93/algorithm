#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

drc = [[-1,0],[1,0],[0,-1],[0,1]]

R,C= map(int,input().split())
# arr=[list(map(str,input().split())) for _ in range(R)]
arr=[input().split() for _ in range(R)]
k = arr[1][1]
for i in range(1,3):
    print(arr[1-i][1])
for j in range(1,3):
    print(arr[1][1-j])
#
# # R,C= map(int,input().split())
# # arr=[input().split() for _ in range(R)]
# r=1
# c=1
# # for k in range(4):
# #     nr = r + dr[k]
# #     nc = c + dc[k]
# #     print(arr[nr][nc])
#
# # if nr>=0 and nr<R and nc >= 0 and nc <C :