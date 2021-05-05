def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        min_distance = 987654321
        current = 0
        remove_cnt = 0

        for rock in rocks:
            diff = rock - current
            if diff < mid:
                remove_cnt += 1
            else:
                current = rock
                min_distance = min(min_distance, diff)

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))