# def solution(genres, plays):
#     answer = []
#     genresSumDic = {}
#     genresPlaysDic = {}
#     for i in range(len(genres)):
#         if genres[i] not in genresSumDic:
#             genresSumDic[genres[i]] = int(plays[i])
#             genresPlaysDic[genres[i]] = [int(plays[i])]
#         else:
#             genresSumDic[genres[i]] += int(plays[i])
#             genresPlaysDic[genres[i]] += [int(plays[i])]
#     MaxGenre = ''
#     for i in range(len(genresSumDic)):
#         MaxGenre = max(genresSumDic)
#         genresSumDic.pop(MaxGenre)
#         if len(genresPlaysDic[MaxGenre]) > 1:
#             genresPlaysDic[MaxGenre].sort()
#             print(genresPlaysDic[MaxGenre])
#             # for i in range(-1,-3,-1):
#             #     answer += [plays.index((genresPlaysDic[MaxGenre][i]))]
#         else:
#             answer += [plays.index((genresPlaysDic[MaxGenre][0]))]
#     return answer
from operator import itemgetter, attrgetter
def solution(genres, plays):
    answer = []
    genresSumDic = {}
    playsDic = {}
    for genre, play in zip(genres,plays):
        genresSumDic[genre] = int(play)
    genresSumDic2 = sorted(genresSumDic.items(), reverse=True, key=lambda item:item[1])

    for i in range(len(genres)):
        if genres[i] not in playsDic:
            playsDic[genres[i]] = [(i,int(plays[i]))]
        else:
            playsDic[genres[i]] += [(i,int(plays[i]))]
    for j in playsDic.values():
        j.sort(key=itemgetter(1), reverse=True)
    for z in range(len(genresSumDic2)):
        for x in range(2):
            answer += [playsDic[genresSumDic2[z][0]][x][0]]
    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = ['500', '600', '150', '800', '2500']

solution(genres,plays)