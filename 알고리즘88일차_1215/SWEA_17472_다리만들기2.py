import collections

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def numbering(idx):
    global q
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0 and arr[nr][nc] == 1:
                arr[nr][nc] = idx
                visit[nr][nc] = 1
                q += [(nr, nc)]


def i2i(r, c, dir, idx):
    cnt = 1
    flag = False
    while 1:
        r += dr[dir]
        c += dc[dir]
        if 0 <= r < N and 0 <= c < M:
            if arr[r][c] != idx and arr[r][c]:
                if idx_visit[arr[r][c]] == 0 :
                    flag = True
                    break
                else:
                    cnt = 1
                    flag = True
                    break
            else:
                cnt += 1
        else:
            break
    if flag and cnt != 1:
        if island_map[idx][arr[r][c]] == 0:
            island_map[idx][arr[r][c]] = cnt
        else:
            island_map[idx][arr[r][c]] = min(cnt, island_map[idx][arr[r][c]])


def island_check(tmp):
    global q
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if arr[nr][nc] == tmp:
                    visit[nr][nc] = 1
                    q += [(nr, nc)]
                elif arr[nr][nc] == 0:
                    i2i(nr, nc, i, tmp)

dr2 = [1,-1,0,0,1,1,-1,-1]
dc2 = [0,0,1,-1,1,-1,1,-1]

def check_bridge(arr):
    global result, flag, idx, q2
    check_idx = [[0]*idx for _ in range(idx)]
    visit_bridge = [[0]*idx for _ in range(idx)]
    temp = 0
    cnt = 1
    for i in range(len(arr)):
        if arr[i] == 1:
            temp += island_len[i][0]
            check_idx[island_len[i][1]][island_len[i][2]] = 1
            if i == 0:
                q2 += [(island_len[i][1],island_len[i][2])]
                visit_bridge[island_len[i][1]][island_len[i][2]] = 1
    while q2:
        r,c = q2.popleft()
        for i in range(8):
            nr = r + dr2[i]
            nc = c + dc2[i]
            if 0 <= nr < idx and 0 <= nc < idx and visit_bridge[nr][nc] == 0 and check_idx[nr][nc] == 1:
                visit_bridge[nr][nc] = 1
                cnt += 1
                q2 += [(nr,nc)]
    if cnt == (idx-2):
        flag = True
        result = min(result, temp)

    # check_idx = []
    # cont = 0
    # tmp = 0
    # for i in range(len(arr)):
    #     if arr[i] == 1:
    #         tmp += island_len[i][0]
    #         if len(check_idx) == 0:
    #             cont += 1
    #             check_idx += [island_len[i][1], island_len[i][2]]
    #         else:
    #             for j in range(1, 3):
    #                 if island_len[i][j] in check_idx:
    #                     cont += 1
    #                     check_idx += [island_len[i][1], island_len[i][2]]
    #                     break
    # if cont == (idx - 2):
    #     flag = True
    #     result = min(result, tmp)


def comb(idx, cnt):
    global select
    if cnt == bridge:
        check_bridge(select)
        return
    if idx >= len(island_len):
        return
    select[idx] = 1
    comb(idx + 1, cnt + 1)
    select[idx] = 0
    comb(idx + 1, cnt)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
q = collections.deque([])
q2 = collections.deque([])
idx = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            arr[i][j] = idx
            q += [(i, j)]
            numbering(idx)
            idx += 1

island_len = []
island_map = [[0] * (idx) for _ in range(idx)]
idx_visit = [0] * idx
tmp = 1
visit = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == tmp and visit[i][j] == 0:
            idx_visit[tmp] = 1
            if sum(idx_visit) == (len(idx_visit) - 1):
                pass
            else:
                q += [(i, j)]
                island_check(tmp)
                tmp += 1
for i in range(idx):
    for j in range(idx):
        if island_map[i][j]:
            island_len += [(island_map[i][j], i, j)]
select = [0] * len(island_len)
bridge = idx - 2
flag = False
result = 987654321
if len(island_len) >= bridge:
    comb(0, 0)

for i in range(N):
    print(arr[i])
print(idx-1)
print(island_len)
if flag:
    print(result)
else:
    print(-1)

