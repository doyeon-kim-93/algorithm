def solve_RCS(ix, co, p):
    result = []
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                if p == 1:
                    result.append((R, C, S))
                else:
                    temp = R * (ix[0][0]) + C * (ix[0][1]) + S * (ix[0][2])
                    if temp == co[1]:
                        result.append((R, C, S))

    for ind in range(2, p):
        t1, t2, t3 = ix[ind - 1]
        temp_li = []

        for R, C, S in result:
            if R * t1 + C * t2 + S * t3 == co[ind]:
                temp_li.append((R, C, S))
        result = temp_li
    return result


T = int(input())
list_index = ['(', ')', '{', '}', '[', ']']
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = [input() for _ in range(N)]
    arr2 = [input() for _ in range(M)]
    arr_index = [[0] * 3 for _ in range(N)]
    arr_come = [0] * N
    rcs_count = [0, 0, 0]
    for i in range(N):
        for k in arr1[i]:
            if k in list_index:
                temp = list_index.index(k)
                inx = temp // 2
                sub = temp % 2
                if sub:
                    rcs_count[inx] -= 1
                else:
                    rcs_count[inx] += 1
        arr_index[i] = rcs_count[:]
    for i in range(N):
        cnt = 0
        while arr1[i][cnt] == '.':
            cnt += 1
        arr_come[i] = cnt

    total = solve_RCS(arr_index, arr_come, N)

    result = [0] * M
    arr2_index = [[0] * 3 for _ in range(M)]
    rcs_count2 = [0, 0, 0]
    for i in range(M):
        for k in arr2[i]:
            if k in list_index:
                temp = list_index.index(k)
                inx = temp // 2
                sub = temp % 2
                if sub:
                    rcs_count2[inx] -= 1
                else:
                    rcs_count2[inx] += 1
            arr2_index[i] = rcs_count2[:]

    for i in range(1, M):
        t1, t2, t3 = arr2_index[i - 1]
        if total:
            R, C, S = total[0]
            ans = R * t1 + C * t2 + S * t3
            for x in total[1:]:
                R, C, S = x
                if R * t1 + C * t2 + S * t3 != ans:
                    result[i] = -1
                    break
            if result[i] != -1:
                result[i] = ans
        else:
            result[i] = -1
            break

    print('#{} '.format(tc), end='')
    print(*result)