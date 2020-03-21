# def che(k):
#     if k == 0 :
#         return 1
#     elif k == 1 :
#         return 1
#     elif k == 2 :
#         return 2
#     else:
#         return che(k-1) + che(k-2)
# N = int(input())
# print(che(N)%10007)

N = int(input())
li = [0] * 1001
li[1] = 1
li[2] = 2
for i in range(3,1001):
    li[i] = li[i-1] + li[i-2]
print(li[N]%10007)