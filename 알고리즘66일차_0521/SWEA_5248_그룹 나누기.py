def Find_Set(x):
    if x == Parent[x]:
        return x
    else:
        return Find_Set(Parent[x])

def Union(x,y):
    Parent[Find_Set(y)] = Find_Set(x)

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Parent = [0]*(N+1)
    for i in range(1, N+1):
        Parent[i] = i
    arr = list(map(int, input().split()))
    for i in range(M):
        start = arr[2*i]
        end = arr[2*i+1]
        Union(start, end)
    result = []
    for i in range(len(Parent)):
        result.append(Find_Set(i))

    print('#%d %d'%(tc, len(set(result))-1))