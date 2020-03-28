N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
result = []

def tree(x, y, n):
    global result
    color = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
               result.append("(")
               tree(x, y, n//2)
               tree(x, y+n//2, n//2)
               tree(x+n//2, y, n//2)
               tree(x+n//2, y+n//2, n//2)
               result.append(")")
               return
    result.append(str(color))


tree(0, 0, N)
print("".join(result))


