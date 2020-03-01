def check(k):
    global result_cnt
    if k == exer:
        #3개월 표시가 찾기
        for i in range(12):
            #3개월
            if plan_board[i] == 3:
                if (0<=i+1<12 and plan_board[i+1] == 3) and (0<=i+2<12 and plan_board[i+2]==3) :
                    plan_board[i+1] = plan_board[i+2] = 0
                if i == 10:
                    if plan_board[i] == 3 and plan_board[i + 1] == 3:
                        plan_board[i + 1] = 0
        cnt = 0
        for m in range(12):
            if plan_board[m] > 0:
                if plan_board[m] == 1:
                    cnt += (plan[m] * price[0])
                elif plan_board[m] == 2:
                    cnt += price[1]
                elif plan_board[m] == 3:
                    cnt += price[2]
        if cnt < result_cnt:
            result_cnt = cnt
    else:
        for j in range(1,4):
            for z in range(12):
                if plan[z] > 0 and plan_board[z] == 0 :
                    plan_board[z] = j
                    check(k + 1)
                    plan_board[z] = 0

T= int(input())
for tc in range(1,T+1):
    price = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    exer = 0 # 월 1회 이상 운동하는 달 표시
    for n in range(12):
        if plan[n] > 0:
            exer += 1
    plan_board = [0]*12
    num = [1,2,3] # 1일은 1/ 1달은 2/ 3개월은 3
    result_cnt = price[3] #1년 이용권  가격
    check(0) #탐색시작
    print(result_cnt)