#4 9 11 23 2 19 7를 가진 리스트를 선언하고
#11값을 찾을 때 걸리는 횟수와 과정을 출력
#10을 찾을 때 걸리는 횟수와 과정을 출력

# 순차검색
k=10
li = [4,9,11,23,2,19,7]
sum_= 0
for i in li:
    sum_ += 1
    if i == k:
        print('{}'.format(k))
        print(sum_)
        break
if k not in li:
    print('{0}는 없어요' .format(k))
    print(sum_)

k= 11
lis = [4,9,11,23,2,19,7]
li = sorted(lis)
sum_=0
for i in li:
    sum_ += 1
    if i == k:
        print('{}'.format(k))
        print(sum_)
        break
if k not in li:
    print('{0}는 없어요' .format(k))
    print(sum_)


