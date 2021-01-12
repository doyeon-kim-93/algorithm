def solution(genres, plays):
    answer = []
    genres_set = {}
    idx = 0
    for genre in genres:
        if genre not in genres_set:
            genres_set[genre] = idx
            idx += 1
    # 장르의 합을 저장한다.
    genres_sum = [[i,0] for i in range(len(genres_set))]
    genres_arr = [[] for _ in range(len(genres_set))]
    for i in range(len(plays)):
        genres_sum[genres_set[genres[i]]][1] += plays[i]
        genres_arr[genres_set[genres[i]]].insert(0,(i,plays[i]))
    #장르 별 앨범을 플레이 순으로 정렬 한다.
    genres_sum.sort(key=lambda x:x[1])
    while genres_sum:
        idx,sumValue = genres_sum.pop()
        genres_arr[idx].sort(key=lambda x:x[1])
        genres_arr[idx].reverse()
        if len(genres_arr[idx]) == 1:
            answer += [genres_arr[idx][0][0]]
        elif len(genres_arr[idx]) > 1:
            for i in range(2):
                answer += [genres_arr[idx][i][0]]
    return answer

a = ['classic','classic','classic','classic','pop']
b = [500,150,800,800,2500]

print(solution(a,b))