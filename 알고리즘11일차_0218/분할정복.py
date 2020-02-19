def exp(C,n):
    if n == 0: return  1
    if n == 1: return  C
    if n % 2: #홀수
        ret = exp(C,(n-1)//2)
        return ret * ret * C
    else: #짝수
        ret = exp(C, n // 2)
        return ret * ret
print(exp(2,10000000))