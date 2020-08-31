# 2806 N - Queen
def n_queen(r):
    global cnt
    # r: 행의 번호, 각 행에서 queen이 놓일 수 있는 자리 확인, 놓을 수 있다면
    # 그 퀸이 영향을 미치는 모든 칸에 표시하고, 다음행으로 진행
    if r == N:  #행의 끝까지 진행했음. N개의 퀸을 모두 놓았음
        cnt += 1
        return

    #행의 모든 칸을 조사해서 유망한 칸이 있다면, 진행, 아니면 종료
    for i in range(N):
        if check[r][i] == 0:    # 표시가 되지 않음, 유망하다.(퀸을 놓을 수 있음)
            # 퀸을 놓음
            marking(r,i)
            #다음 행으로 진행
            n_queen(r+1)
            un_marking(r,i)


def marking(r,c):  #퀸을 놓았을 때, 해당 퀸이 영향을 미치는 칸에 표시
    # 델타를 이용한 마킹
    # 8방 , 12시 방향부터 시계방향으로
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]

    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        while True:
            if 0<= nr <N and 0<= nc < N:
                check[nr][nc] += 1
                nr += dr[d]
                nc += dc[d]
            else:
                break

def un_marking(r,c): #퀸에 의해 영향을 받는 칸 표시 되돌리기
    # 델타를 이용한 마킹
    # 8방 , 12시 방향부터 시계방향으로
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]

        while True:
            if 0 <= nr < N and 0 <= nc < N:
                check[nr][nc] -= 1
                nr += dr[d]
                nc += dc[d]
            else:
                break


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    check = [[0] * N for _ in range(N)]
    cnt = 0
    n_queen(0)
    print("#{} {}".format(tc,cnt))