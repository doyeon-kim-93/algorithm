def solution(clothes):
    clothesList = {}
    result = 1
    for i in range(len(clothes)):
        if clothes[i][1] not in clothesList:
            clothesList[clothes[i][1]] = [clothes[i][0]]
        else:
            clothesList[clothes[i][1]] += [clothes[i][0]]
    for key in clothesList:
        result *= (len(clothesList[key])+1)
    return result -1



cloth = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(cloth))