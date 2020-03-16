T = int(input())
for tc in range(1,T+1):
    con = list(input())
    che = []
    che2 = []
    if len(con)%2 == 0:
        for i in range((len(con)//2)):
            che += [con[i]]
        for i in range(len(con)-1,(len(con)//2)-1,-1):
            che2 += [con[i]]
    else:
        for i in range((len(con)//2)+1):
            che += [con[i]]
        for i in range(len(con)-1,(len(con)//2)-1,-1):
            che2 += [con[i]]
    flag = True
    for j in range(len(che)):
        if che[j] == '?' or che2[j] == '?':
            continue
        elif che[j] != che2[j]:
            print('#{} Not exist'.format(tc))
            flag = False
            break
    if flag:
        print('#{} Exist'.format(tc))