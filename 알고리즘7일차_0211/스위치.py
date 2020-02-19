N = int(input())
a = [50]
rr = list(map(int, input().split()))
arr = a + rr
people = int(input())
action = [list(map(int, input().split())) for _ in range(people)]

for i in range(people):
    if action[i][0] == 1:
        for j in range(1,len(arr)):
            if j % action[i][1] == 0:
                arr[j] ^= 1

    else:
        for j in range(1,len(arr)):
            if j == action[i][1]:
                arr[j] ^= 1
                k = 1
                while 1:
                    if 1 <= j - k <= len(arr)-1 and 1 <= j + k <= len(arr)-1:
                        if arr[j-k] == arr[j+k]:
                            arr[j-k] ^= 1
                            arr[j+k] ^= 1
                            k += 1
                        else:
                            break
                    else:
                        break
for i in range(1,len(arr)):
    if i % 20==0:
        print(arr[i], end = ' ')
        print('\b', end = '')
        print()
    else:
        print(arr[i], end=' ')
print('\b',end = '')
# cnt=0
# while text:
#     if cnt%20:
#         pass # 20번마다 한번씩 동작
#     print(text[cnt],end=' ')
#
#     cnt+=1