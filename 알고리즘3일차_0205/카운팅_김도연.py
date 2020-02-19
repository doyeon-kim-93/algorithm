T = int(input())
for tc in range(1,T+1):
    card = input()
    game_card = list(range(1,14))
    dic_ = {'S':0 ,'D':0, 'H':0, 'C':0}
    for i in range(len(card)):
        if card[i] == 'S':
            dic_['S'] = int(card[i+1:i+3])
        if card[i] == 'D':
            dic_['D'] = int(card[i+1:i+3])
        if card[i] == 'H':
            dic_['H'] = int(card[i+1:i+3])
        if card[i] == 'C':
            dic_['C'] = int(card[i+1:i+3])
    dic_2 = dic_
    S_game_card = []
    D_game_card = []
    H_game_card = []
    C_game_card = []
    for key, value in dic_2.items():
        for i in range(len(game_card)):
            if key == 'S':
                if value != game_card[i]:
                    S_game_card.append(game_card[i])
            if key == 'D':
                if value != game_card[i]:
                    D_game_card.append(game_card[i])
            if key == 'H':
                if value != game_card[i]:
                    H_game_card.append(game_card[i])
            if key == 'C':
                if value != game_card[i]:
                    C_game_card.append(game_card[i])

    re_s = len(S_game_card)
    re_d = len(D_game_card)
    re_h = len(H_game_card)
    re_c = len(C_game_card)

    print('#{} {} {} {} {}'.format(tc,re_s,re_d,re_h,re_c))