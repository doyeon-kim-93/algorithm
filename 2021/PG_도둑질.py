def solution(money):
    #첫번째 집 선택
    table = [0 for _ in range(len(money))]
    table[0] = money[0]
    table[1] = table[0]
    for i in range(2,len(money)-1):
        table[i] = max(table[i-1],table[i-2]+money[i])
    # 두번째 집 부터 선택
    table2 = [0 for _ in range(len(money))]
    table2[1] = money[1]
    for i in range(2,len(money)):
        table2[i] = max(table2[i-1],table2[i-2]+money[i])
    answer = max(max(table),max(table2))
    return answer