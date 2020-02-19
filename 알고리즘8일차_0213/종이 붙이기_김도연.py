def get_sum(x):
    if x == N :
        return 1
    if x > N:
        return 0
    return get_sum(x+10) + get_sum(x+20)*2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print("#{} {}".format(tc,get_sum(0)))