import sys
sys.stdin = open("input.txt", "r")

def chek(k,z):
    global result,B,N
    if k >= B:
        result = min(result,k)
        return
    elif k >= result:
        return
    else:
        for i in range(z,N):
            if visit[i] == 0:
                visit[i] = 1
                chek(k+arr[i],i)
                visit[i] = 0

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    arr = list(map(int,input().split()))
    result = 9876543621
    visit = [0] * N
    chek(0,0)
    print('#{} {}'.format(tc,(result-B)))