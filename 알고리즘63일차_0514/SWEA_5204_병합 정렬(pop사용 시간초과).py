def MergeSort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = MergeSort(left)
    right = MergeSort(right)
    if left[-1] > right[-1]:
        cnt +=1
    return Merge(left, right)

def Merge(arr1, arr2):
    result = []
    while arr1 or arr2:
        if arr1 and arr2:
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        elif arr1:
            result.append(arr1.pop(0))
        elif arr2:
            result.append(arr2.pop(0))
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    re_arr = sorted(arr)
    cnt = 0
    MergeSort(arr)
    print('#{} {} {}'.format(tc,re_arr[N//2],cnt))