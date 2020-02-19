# def fac(N):
#     if N == 1:
#         return 1
#     return fac(N-1) * N
#
# print(fac(5000))

K = int(input())
result = 1
for i in range(1,K+1):
    result *= i
print(result)