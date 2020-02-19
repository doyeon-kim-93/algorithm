#1~10까지 주어졌을 때 부분집합의 합이 11이 되는 경우를 모두 출력 하시오.
# li=list(range(1,11))
# N=len(li)
#
# for i in range(1<<N):
#     result = []
#     for j in range(N):
#         if i&(1<<j):
#             result.append(li[j])
#     if sum(result) ==11:
#         print(result)


li=list(range(1,11))
N=len(li)

for i in range(1<<N):
    sum = 0
    result = []
    for j in range(N):
        if i&(1<<j):
            sum +=li[j]
            result.append(li[j])
    if sum == 11:
        print(result)