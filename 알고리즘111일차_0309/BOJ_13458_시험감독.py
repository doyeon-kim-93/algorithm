N = int(input())
classList = list(map(int,input().split()))
B,C = map(int,input().split())
cnt = 0
for classN in classList:
    cntN = 0
    if classN >= B:
        remainN = classN - B
        cntN += 1
        if remainN:
            if remainN >= C:
                n = remainN/C
                if (remainN//C) < n < (remainN//C)+1:
                    cntN += (remainN//C+1)
                else:
                    cntN += (remainN//C)
            else:
                cntN += 1
    else:
        cntN += 1
    cnt += cntN
print(cnt)
