import sys
sys.stdin = open("input (6).txt", "r")


for i in range(10):
    T = int(input())
    #행 리스트 100개씩 묶어 받기
    arr = []
    for i in range(100):
        arr.append(list(map(int,input().split())))
    #행의 합
    hori_result = []
    for j in range(100):
        hori_sum = sum(arr[j])
        hori_result.append(hori_sum)
    max_hori = max(hori_result)
    #열 나열
    verti_ar = []
    for i in range(100):
        for j in range(100):
            verti_ar.append(arr[j][i])
    # #열 리스트 100개씩 묶기
    verti_arr =[]
    for n in range(100):
        verti_arr.append(verti_ar[0:100])
        for j in range(100):
            verti_ar.remove(verti_ar[0])

    # #열의 합
    verti_result = []
    for j in range(100):
        verti_sum = sum(verti_arr[j])
        verti_result.append(verti_sum)
    max_verti = max(verti_result)
    #왼쪽 대각선의 합
    l_cross = []
    for i in range(100):
        l_cross.append(arr[i][i])
    l_cross_sum = sum(l_cross)
    r_cross = []
    for i in range(100):
        l_cross.append(arr[i][99-i])
    R_cross_sum = sum(r_cross)

    
    result = [max_hori,max_verti,l_cross_sum,R_cross_sum]
    print(result)
    print('#{} {}'.format(T, max(result)))