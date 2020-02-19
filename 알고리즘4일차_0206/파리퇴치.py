T = int(input())
for tc in range(1,T+1):
    N ,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)] #파리 배열

#파리 퇴치 시작
    while 1:
        flag = False
        dr = 0 #행의 값을 변화
        dc = 0 #열의 값을 변환
        k = M+dr #행의 값
        L = M+dc #열의 값
        max_num = 0
        sum_ = 0
        for i in range(dr, k):
            for j in range(dc, L):
                sum_ += arr[i][j] #값을 계속 더해감
            if arr[i][j] == arr[N-1][N-1]: #만일 파리채의 제일 마직막 값이 전체 배열(N)의 마지막 값과 같을 때 반복문을 이탈하기 위해 flag 변환
                flag = True
            if arr[i][j] == arr[k-1][L-1]: #파리채 값이 1패턴 돌았다면 옆으로 이동
                dc += 1
                break
            if arr[i][j] == arr[k-1][N-1]: #파리채가 한열을 전부 탐색했다면 다음 열로 이동
                dr += 1
                L = M
                dc = 0
                break

        if max_num < sum_: #최대값을 계속 갱신
            max_num = sum_

        if flag: # while문 이탈
            break

    print(max_num)


