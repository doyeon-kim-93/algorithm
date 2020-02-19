# T = int(input())
# for n in range(1,T+1):
#     a =int(input())
#     li=input()
#     card=[]
#     for i in li:
#         card.append(i)
#     result={}
#     for k in range(a):
#         if card[k] in result:
#             result[card[k]] += 1
#         else:
#             result[card[k]] = 1
#     val=list(result.values())
#     key_=list(result.keys())
#     result2=[0]
#     for key, value in result.items():
#         if max(val) == value:
#             x = key
#             y = value
#             result2[-1]=int(x)
#             for key2, value2 in result.items():
#                 if y == value2:
#                     if int(key2)>int(key):
#                         if result2[-1]<=int(key2):
#                             result2[-1]=int(key2)
#
#     result_key = str(result2[0])
#     print(f'#{n} {result_key} {result[result_key]} ')

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    line = input()

    nums = [0]*10
    for i in range(len(line)):
        nums[int(line[i])] += 1
    max_idx = 0
    max_value = 0
    for i in range(len(nums)-1 ,-1,-1):
        #지금은 뒤에서 검사를 하기 때문에 조건 <만 검사
        #앞에서 부터 검사한다고 하면 <= 으로 검사
        #문제에서 같으 장수를 가지면 큰수를 출력한가고 했기 때문
        if max_value < nums[i]:
            max_value = nums[i]
            max_udx = i
    print("#{} {} {}".format(tc,max_idx,max_value))