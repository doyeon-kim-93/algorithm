import collections

def parent(k):
    global n1_parent
    p1 = pa[k]
    for z in range(10001) :
        if len(p1) > 0:
            n1_parent.append(p1[0])
            p1 = pa[p1[0]]
        else:
            break
def search(k):
    global result,q
    for z in ch[k]:
        q += [z]
    while q:
        n = q.popleft()
        result += 1
        if len(ch[n]) != 0:
            for x in ch[n]:
                q += [x]

T = int(input())
for tc in range(1,T+1):
    V,E,n1,n2 = map(int,input().split())
    arr = list(map(int,input().split()))
    pa =[[] for _ in range(V+1)]
    ch =[[] for _ in range(V+1)]
    for i in range(0,(2*E),2):
            pa[arr[i+1]] += [arr[i]]
            ch[arr[i]].append(arr[i+1])
    n1_parent = []
    parent(n1)
    parent(n2)
    result_parent = 0
    for z in range(0,len(n1_parent)):
        flag = False
        for j in range(z+1,len(n1_parent)):
            if n1_parent[z] == n1_parent[j]:
                result_parent = n1_parent[z]
                flag = True
                break
        if flag:
            break
    q = collections.deque([])
    result = 1
    search(result_parent)
    print('#{} {} {}'.format(tc,result_parent,result))
