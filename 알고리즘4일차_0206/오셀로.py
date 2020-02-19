def con(k):
    k = [a,b,z]
    r = [-1, 0, 1, 1, 1, 0, -1, -1]
    c = [-1, -1, -1, 0, 1, 1, 1, 0]
    search = []
    if z = 1:
        con = 2
        for i in range(8):
            if arr[a + r[i]][b + c[i]] == con:
                search.append(arr[a + r[i]][b + c[i]])
    else:
        con =1
        for i in range(8):
            if arr[a + r[i]][b + c[i]] == con:
                search.append(arr[a + r[i]][b + c[i]])

T = int(input())
for tc in range(1,T+1):
