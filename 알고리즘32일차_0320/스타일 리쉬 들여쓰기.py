import sys
sys.stdin = open("sample_input (12).txt", "r")
def check(k,t,li):
    if k == '(':
        li[t][0] += 1
    elif k == ')':
        li[t][1] += 1
    elif k == '[':
        li[t][2] += 1
    elif k == ']':
        li[t][3] += 1
    elif k == '{':
        li[t][4] += 1
    elif k == '}':
        li[t][5] += 1

for tc in range(1,int(input())):
    p, q = map(int,input().split())
    pro = [list(input()) for _ in range(p)]
    me = [list(input()) for _ in range(q)]
    pro_che = [[0]*6 for _ in range(p)]
    me_che = [[0]*6 for _ in range(q)]
    for i in range(p):
        for j in range(len(pro[i])):
            check(pro[i][j],i,pro_che)
    for i in range(q):
        for j in range(len(me[i])):
            check(me[i][j],i,me_che)
    print(pro_che)
    print(me_che)

