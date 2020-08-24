#흰색,파란색,빨간색의 모든 조합을 구해서
#모든 경우의 수에 대해서 수정해야 하는 칸의 개수를 센다.
# 조합문제 >>> 일반적인 조합문제 보다는 쉽다
# 선택해야 하는 개수가 정해저 있음 >> 2개
# 반복문으로도 처리가 가능함
# 흰색줄의 범위 (0번~끝에서 3번째 까지)
# 파란색줄의 범위(흰색 다음부터, 끝에서 두 번째 까지)
# 빨간색 줄의 범위(파란색 다음부터 끝까지)
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    flag = [input() for _ in range(N)]
    result = 2500   # 모든 칸을 다 바꾼다고 가정하면 최대 2500번
    #깃발 범위 나누기
    #흰색 부분이 가능한 모든 부분을 반복문으로 순회
    for i in range(0,N-2): #최소 2칸은 남아야 함
        #파란색 영역
        for j in range(i+1,N-1):
            #각 부분의 색깔별로, 바꾸어야 할 개수 세기
            cnt = 0 # 바꾸는 칸의 개수를 세기 위한 변수
            # 영역의 크기는 정해진 상황
            # 흰색 몇칸 바꿔야 하는지
            # 흰색 영역 순회하면서, 흰색이 아닌 칸개수 세기
            for w in range(i+1):
                for k in range(M):
                    if flag[w][k] != 'W':
                        cnt+= 1
            # 파란색 몇칸 바꿔야 하는지
            for b in range(i+1,j+1):
                for k in range(M):
                    if flag[b][k] != 'B':
                        cnt += 1
            # 빨간색 몇칸 바꿔야 하는지
            for r in range(j+1,N):
                for k in range(M):
                    if flag[r][k] != 'R':
                        cnt+=1

            #cnt : 몇칸 바꿔야 되는지 저장되어 있음
            if cnt < result:
                result = cnt
    print("#{} {}".format(tc,result))