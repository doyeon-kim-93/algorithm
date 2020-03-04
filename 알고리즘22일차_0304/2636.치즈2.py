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
                for z in range(4):
                    nn = nr + dr[z]
                    nm = nc + dc[z]
                    if 0 <= nn < H and 0 <= nm < W:
                        if arr[nn][nm] == 1 :
                            arr[nn][nm] = 0
                            cheeze -= 1
                nocheese(nr,nc)
# def melt(cnt):
#     global cheeze
#     nocheese(0, 0)
#     if cheeze == 0:
#         print(cnt)
#         return
#     else:
#         cnt += 1
#         melt(cnt)

H, W = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(H)]
cheeze = 0
for i in range(H):
    cheeze += sum(arr[i])
nocheese(0,0)
for x in range(H):
    print(arr[x])