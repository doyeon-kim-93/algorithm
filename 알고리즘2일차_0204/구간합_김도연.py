# T = int(input())
# for n in range(1, T + 1):
#     y = list(map(int, input().split()))
#     a, b = y[0], y[1]
#     li = list(map(int, input().split()))
#     result = []
#     for i in range(0, (a - b) + 1):
#         k = b
#         sum_ = 0
#         for j in range(b):
#             sum_u = li[i + j]
#             sum_ += sum_u
#         result.append(sum_)
#
#     print(f'#{n} {max(result)-min(result)}')

def slice(nums):
    maxvalue = 0
    minvalue = 987654321

    for i in range(N-M+1):
        sum = 0
        for j in range(i,i+M):
            sum += nums[j]
        if maxvalue < sum:
            maxvalue = sum
        if minvalue > sum:
            minvalue = sum
    return maxvalue - minvalue

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    nums = map(int,input().split())

    print("#{} {}".format(tc, slice(nums)))