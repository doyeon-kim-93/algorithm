#재귀로 반복문 표현
# for i in range(3):
#     print('HELLOW')
#
# def printHELL(n):
#     if n == 1:
#         print('HELLOW')
#     else:
#         print('HELLOW')
#         printHELL(n-1)
# printHELL(3)
#
# def printHELL(n):
#     if n < 3:
#         print('HELLOW')
#         printHELL(n+1)
# printHELL(0)
# def printHELL(n):
#     if n == 3:
#         return
#     else:
#         print('HELLOW')
#         printHELL(n+1)
# printHELL(0)

### 백트래킹
# def printHELL(i,n):
#     if i == n:
#         return
#     else:
#         print('HELLOW', i)
#         printHELL(i+1,n)
#         print('HELLOW',i)
# printHELL(0,3)
#
# cnt = 0
# def printHEIIO(i,n):
#     if i == n:
#         global cnt
#         cnt += 1
#     else:
#         printHEIIO(i+1,n)
#         printHEIIO(i+1,n)
# printHEIIO(0,3)
# print('cnt= ', cnt)
#----------------------------------------------------------------------------------
path = [0] * 3
def printHEIIO(i,n):
    if i == n:
        print(path)
    else:
        path[i] = 1
        printHEIIO(i+1,n)
        path[i] = 0
        printHEIIO(i+1,n)
printHEIIO(0,3)
print()

N = 3
bit = [0] * N
for i in range(2):
    bit[0] = i
    for i in range(2):
        bit[1] = i
        for i in range(2):
            bit[2] = i
            print(bit)
print()
def subset(k,n):
    if k == n:
        print(bit)
    else:
        for i in range(2):
            bit[k] = i
            subset(k+1,n)
subset(0,N)