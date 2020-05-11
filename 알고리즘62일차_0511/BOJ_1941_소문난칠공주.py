import sys

sys.stdin = open('../input.txt', 'r')
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def find_SP(k, s, som, pre):
    global cnt
    if k == 4 and som == 0:
        return
    if k == 5 and som == 1:
        return
    if k == 6 and som == 2:
        return
    if k == 7 and som >= 4:
        cnt += 1
        print(pick)
        return
    for x in range(s, 25):
        if not pick:
            i = x % 5
            j = x // 5
            pick.append((seats[j][i], x))
            pre = x
            if seats[j][i] == 'S':
                find_SP(k + 1, s + 1, som + 1, pre)
            else:
                find_SP(k + 1, s + 1, som, pre)
            pick.pop()

        elif x == pre + 1 or pre + 5:
            i = x % 5
            j = x // 5
            tmp = pre
            pick.append((seats[j][i], x))
            pre = x
            if seats[j][i] == 'S':
                find_SP(k + 1, s + 1, som + 1, pre)
            else:
                find_SP(k + 1, s + 1, som, pre)
            pick.pop()
            pre = tmp


pick = []
N = 5
seats = [input() for _ in range(N)]
cnt = 0
find_SP(0, 0, 0, 0)
