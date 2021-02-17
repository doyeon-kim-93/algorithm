def check(begin, target, words,visit,cnt):
    global result
    if begin == target:
        result = min(result,cnt)
        return
    elif cnt >= result:
        return
    else:
        for i,word in enumerate(words):
            # print('cnt:',cnt,123,visit,begin,word)
            tmp = 0
            if visit[i] == 0:
                for j in range(len(word)):
                    if begin[j] == word[j]:
                        tmp += 1
                if tmp == 2:
                    visit[i] = 1
                    check(word, target, words, visit, cnt+1)
                    visit[i] = 0
                    # print('cnt:', cnt, 456,visit,begin,word)

def solution(begin, target, words):
    global result
    result = 987654321
    if not begin:
        return
    answer = 0
    visit = [0] * len(words)
    cnt = 0
    for i,word in enumerate(words):
        if word == begin:
            visit[i] = 1
        elif word == target:
            cnt += 1
    if cnt:
        check(begin, target, words,visit,0)
        answer = result
    return answer

result = 98764321

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
print(solution('hit', 'hhh', ['hhh', 'hht']))
print(solution('hit', 'zzz', ['aaa']))
print(solution('hit', 'zzz', ['zzz', 'zyz', 'xzz', 'xyz', 'hyt', 'hyz', 'xiz', 'hiz']))

print(solution('aaa', 'abc', ['aaz', 'aab', 'abb', 'abc']))
