T = int(input())
pattern = {'S':0 ,'D':1, 'H':2, 'C':3}

for tc in range(1,T+1):
    line = input()

    card = [[0]*14 for _ in range(4)]
    flag = True
    for i in range(0,len(line),3):
        card_pattern = pattern[line[i]]
        card_num = int(line[i+1:i+3])
        if card[card_pattern][card_num] == 1:
            flag = False
            break
        card[card_pattern][card_num]= 1
        card[card_pattern][0] += 1

    print("#{}".format(tc), end=" ")
    if flag:
        for i in range(4):
            print("{}".format(13 - card[i][0]), end=" ")
        print()
    else:
        print("ERROR")
