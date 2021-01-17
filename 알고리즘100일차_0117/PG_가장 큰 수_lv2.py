def solution(numbers):
    number = sorted(list(map(str, numbers)), key=lambda x:x*5, reverse=True)
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))