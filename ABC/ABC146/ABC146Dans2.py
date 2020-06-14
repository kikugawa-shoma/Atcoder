n = int(input())
node = {i: [] for i in range(1, n + 1)}
visited = [False for i in range(n + 1)]
q = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
    q.append((a, b))

mother = q[0][0]
visited[mother] = True

d = []
e = []

paint = {i: {} for i in range(1, n + 1)}

mother_paint = [0 for i in range(n + 1)]

# 使う要素 node visited paint mother_paint の四つのリスト
c = 1
for child in node[mother]:
    visited[child] = True
    paint[mother][child] = c
    paint[child][mother] = c
    mother_paint[child] = c
    c += 1
    d.append(child)

while d:
    for parent in d:
        p = 1
        for child in node[parent]:
            if visited[child] == False:
                visited[child] = True
                if p != mother_paint[parent]:
                    paint[parent][child] = p
                    paint[child][parent] = p
                    mother_paint[child] = p
                    p += 1
                    e.append(child)
                else:
                    p += 1
                    paint[parent][child] = p
                    paint[child][parent] = p
                    mother_paint[child] = p
                    p += 1
                    e.append(child)
    if e:
        d = e
        e = []
    else:
        d = []
        e = []
K = 0
for i in range(1, n + 1):
    K = max(K, len(node[i]))
print(K)
for i in range(n - 1):
    s, t = q[i][0], q[i][1]
    print(paint[s][t])