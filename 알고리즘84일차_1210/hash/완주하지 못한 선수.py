def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            print(participant[i])
            return participant[i]

    return participant[-1]


k = ["leo", "kiki", "eden"]
s = ["eden", "kiki"]

print(solution(k,s))
