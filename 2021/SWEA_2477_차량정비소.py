import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N,M,K,A,B = map(int,input().split())
    recep = list(map(int,input().split()))
    repair = list(map(int,input().split()))
    departTime = list(map(int,input().split()))
    result = 0
    rec = [[] for _ in range(N)]
    rep = [[] for _ in range(M)]
    wait1 = []
    wait2 = []
    manDesk = [[] for _ in range(K)]
    T = -1
    people = K
    while people:
        T += 1
        #도착 시간에 따른 대기장소1 사람추가
        for i,time in enumerate(departTime):
            if T == time:
                wait1 += [i]
        wait1.sort()
        #접수창고 완료 사람 빼기
        for i in range(len(rec)):
            if rec[i]:
                if rec[i][1] == T:
                    #접수 완료 대기장소2 사람추가
                    wait2 += [[rec[i][0],T,i]]
                    manDesk[rec[i][0]] += [i]
                    rec[i] = []
        #정비창고 완료 사람 빼기
        for i in range(len(rep)):
            if rep[i]:
                if rep[i][1] == T:
                    manDesk[rep[i][0]] += [i]
                    people -= 1
                    rep[i] = []
        wait2.sort(key= lambda x: (x[1],x[2]))
        #사람 서비스 받기!!!
        for i in range(len(rec)):
            if not rec[i]:
                if wait1:
                    manNum = wait1.pop(0)
                    rec[i] += [manNum,T+recep[i]]
        for i in range(len(rep)):
            if not rep[i]:
                if wait2:
                    val = wait2.pop(0)
                    rep[i] += [val[0],T+repair[i]]
    for i,val in enumerate(manDesk):
        if val[0] == A-1 and val[1] == B-1:
            result += (i+1)
    if result == 0:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, result))