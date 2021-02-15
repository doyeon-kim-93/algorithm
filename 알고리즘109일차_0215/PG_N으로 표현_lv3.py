def solution(N, number):
    answer = -1
    if N == number:
        return 1
    s = [set() for _ in range(8)]
    for i in range(8):
        s[i].add(int(str(N)*(i+1)))
    for i in range(1,8):
        for j in range(i):
            for v1 in s[j]:
                for v2 in s[i-j-1]:
                    s[i].add(v1+v2)
                    s[i].add(v1-v2)
                    s[i].add(v1*v2)
                    if v2 != 0:
                        s[i].add(v1//v2)
        if number in s[i]:
            answer = i + 1
            break
    return answer