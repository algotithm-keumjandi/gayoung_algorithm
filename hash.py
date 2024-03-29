# 백준 1620 - hash
N, M = map(int, input().split())

idx_to_name = {}
name_to_idx = {}
for i in range(1, N + 1):
    name = input().rstrip()
    idx_to_name[i] = name
    name_to_idx[name] = i

for j in range(M) :
    q = input().rstrip()
    if q.isdigit():
        print(idx_to_name[int(q)])
    else :
        print(name_to_idx[q])