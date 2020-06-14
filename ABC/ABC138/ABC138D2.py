from collections import deque

class Tree:
    def __init__(self, n, init_list, root=1):
        self.num = (n + 1)
        self.parents = [-1] * self.num
        self.first_child = [-1] * self.num
        self.next_child = [-1] * self.num
        self.check = [-1] * self.num
        self.g = {i: [] for i in range(1, self.num)}
        self.make_g(init_list, root)

    def make_g(self, con, root):
        m = len(con)
        for i in range(m):
            self.g[con[i][0]].append(con[i][1])
            self.g[con[i][1]].append(con[i][0])
        q = deque([root])
        while q:
            node = q.pop()
            self.check[node] = 1
            cnt = 0
            for i, sub_node in enumerate(self.g[node]):
                if self.check[sub_node] != -1:
                    continue
                if cnt == 0:
                    self.first_child[node] = sub_node
                self.parents[sub_node] = node
                if i != len(self.g[node])-1:
                    self.next_child[sub_node] = self.g[node][i+1]
                q.append(sub_node)
                cnt += 1

    def childs(self, node):
        child_list = []
        if self.first_child[node] != -1:
            child_list.append(self.first_child[node])
            node = self.first_child[node]
            while 1:
                if self.next_child[node] == -1:
                    break
                else:
                    child_list.append(self.next_child[node])
                node = self.next_child[node]
        return child_list

    def parent(self, n):
        return self.parents[n]


import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N-1)]
P = [0] * Q
X = [0] * Q
V = [0] * (N + 1)
for i in range(Q):
    P, X = map(int, input().split())
    V[P] += X

tr = Tree(N, AB)
# 800ms

q = deque()
q.extend(tr.childs(1))
while q:
    node = q.pop()
    V[node] += V[tr.parent(node)]
    tmp = tr.childs(node)
    if tmp:
        q.extendleft(tmp)

print(*V[1:])
