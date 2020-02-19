get_word = input('입력하세요')
my_word = input('확인하고 싶은 문자열은?')

getlen = len(get_word)
mylen = len(my_word)
cnt = 0
while 1:
    flag = False
    k = 0
    l = 0
    cnt += 1
    for i in range(k,getlen):
        for j in range(mylen):
            if my_word[j] == get_word[i]:
                l += 1
            else:
                k += 1
                l = 0
                break
    if l >= mylen:
        break

        if i == (getlen -1):
            flag = True
    if flag:
        break
if cnt > 0:
    print('{}번 찾았다'.format(cnt))
else:
    print('없다.')

# A pattern matching algorithm
# rithm