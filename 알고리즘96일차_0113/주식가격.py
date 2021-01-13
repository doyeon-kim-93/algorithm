def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        if i+1 < n:
            cnt = 1
            flag =  True
            for j in range(i+1,n):
                if prices[i] <= prices[j]:
                    cnt += 1
                else:
                    answer += [cnt]
                    flag =  False
                    break
            if flag:
                answer += [cnt-1]
        elif i == n-1:
            answer += [0]
    return answer
a = [1, 2, 3, 2, 3]
print(solution(a))