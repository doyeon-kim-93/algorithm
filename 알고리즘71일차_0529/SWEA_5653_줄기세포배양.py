dr = [0,1,0,-1]
dc = [1,0,-1,0]
def chek(N,M,K,arr):
    day = K//2
    time = [[-1]*(M+K) for _ in range(N+K)]
    cell = [[0]*(M+K) for _ in range(N+K)]
    for i in range(N):
        for j in range(M):
            cell[i+day][j+day] = arr[i][j]
            if arr[i][j] != 0:
                time[i+day][j+day] = 0
    for h in range(1,K+1):#배양시간별 각 칸의 상태 정의
        for i in range(N+K): #줄기세포가 있는 전체 배열 조회
            for j in range(M+K):
        # for i in range(day-h//2,N+day+h//2): #줄기세포가 있는 제일 왼쪽 부터 가장 오른쪽 아래까지
        #     for j in range(day-h//2,M+day+h//2):
                tmp = [] #주변의 활성세포 생명력 리스트
                if cell[i][j] == 0:#아직 세포가 없으면
                    for k in range(4):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if 0<= nr < N+K and 0<= nc < M+K:
                            if cell[nr][nc]>0 and ((h-time[nr][nc])/cell[nr][nc])>1:
                                #활성세포가 있으면
                                tmp.append(cell[nr][nc])#생명력 리스트 만듦
                                cell[i][j] = max(tmp)#ㅅㅔ포생성
                                time[i][j] = h
    cnt = 0
    for i in range(N+K):
        for j in range(M+K):
            if cell[i][j] > 0 and (K-time[i][j])//cell[i][j]<2:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = chek(N,M,K,arr)
    print('#{} {}'.format(tc,result))