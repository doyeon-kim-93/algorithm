import sys
sys.setrecursionlimit(100000)
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def nocheese(r,c):
    global cheeze
    for z in range(4):
        nr = r + dr[z]
        nc = c + dc[z]
        if 0<= nr < H and 0<= nc < W :
            if arr[nr][nc] == 0:
                arr[nr][nc] = 2
                nocheese(nr,nc)

# def melt(sum_,cnt):
#     result = sum_
#     cnt += 1
#     nocheese(0,0)
#     for n in range(H):
#         for m in range(W):
#             if arr[n][m] == -1:
#                 for z in range(4):
#                     nn = n + dr[z]
#                     nm = m + dc[z]
#                     if 0 <= nn < H and 0 <= nm < W:
#                         if arr[nn][nm] == 1 :
#                             arr[nn][nm] = 0
#                             result -= 1
#     if result == 0:
#         print(cnt)
#         print(sum_)
#         return
#     else:
#         melt(result,cnt)
H, W = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(H)]
cheeze = 0
for i in range(H):
    cheeze += sum(arr[i])
print(cheeze)
# melt(cheeze,0)
nocheese(0,0)
for i in range(H):
    for j in range(W):
        if arr[i][j] == 1:
            for z in range(4):
                nn = i + dr[z]
                nm = j + dc[z]
                if 0 <= nn < H and 0 <= nm < W:
                    if arr[nn][nm] == 2 :
                        arr[i][j] = 0
                        cheeze -= 1
                        break

for x in range(H):
    print(arr[x])
print(cheeze)