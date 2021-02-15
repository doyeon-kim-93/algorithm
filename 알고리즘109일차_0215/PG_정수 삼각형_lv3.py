def solution(triangle):
    s = [[[] for _ in range(i)] for i in range(1, len(triangle) + 1)]
    s[0][0].append(triangle[0][0])
    result = triangle[0][0]
    for i in range(len(triangle) - 1):
        for j in range(len(s[i])):
            for num in s[i][j]:
                v1 = num + triangle[i + 1][j]
                v2 = num + triangle[i + 1][j + 1]
                result = max(v1, v2, result)
                if s[i + 1][j]:
                    if s[i + 1][j][0] < v1:
                        s[i + 1][j] = [v1]
                else:
                    s[i + 1][j].append(v1)
                if s[i + 1][j + 1]:
                    if s[i + 1][j + 1][0] < v2:
                        s[i + 1][j + 1] = [v2]
                else:
                    s[i + 1][j + 1].append(v2)
    return result