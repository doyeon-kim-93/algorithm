# def solution(people, limit):
#     answer = 0
#     while people:
#         boat = []
#         maxval = []
#         for i,v in enumerate(people):
#             if not maxval:
#                 maxval += [i,v]
#             else:
#                 if maxval[1] < v:
#                     maxval = [i,v]
#         boat += [maxval[1]]
#         people.pop(maxval[0])
#         lastVal = limit - boat[0]
#         if people:
#             minval = []
#             for i,v in enumerate(people):
#                 if not minval:
#                     if lastVal >= v :
#                         minval += [i,v]
#                 else:
#                     if lastVal >= v > minval[1]:
#                         minval = [i,v]
#             if minval:
#                 boat += [minval[1]]
#                 people.pop(minval[0])
#         if boat:
#             answer += 1
#     return answer
def solution(people, limit):
    answer = 0
    people.sort()
    maxidx = len(people)-1
    minidx = 0
    while minidx <= maxidx:
            lastVal = limit - people[maxidx]
            maxidx -= 1
            if lastVal >= people[minidx]:
                minidx += 1
            answer += 1
    return answer

print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))
