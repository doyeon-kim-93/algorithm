T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = {0}
    for i in arr:
        con = set()
        for j in result:
            con.add(i+j)
        result.update(con)
    print('#{} {}'.format(tc,len(result)))
            
