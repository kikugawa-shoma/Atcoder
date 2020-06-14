#二分探索　＋　BIT木

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 1-indexed　Binary Indexed Tree
class BIT:
    def __init__(self, n, init_list):
        self.num = n + 1
        self.tree = [0] * self.num
        for i, e in enumerate(init_list):
            self.update(i, e)

    def update(self, k, x):
        k = k + 1
        while k < self.num:
            self.tree[k] += x
            k += (k & (-k))
        return

    def query1(self, r):
        ret = 0
        while r > 0:
            ret += self.tree[r]
            r -= r & (-r)
        return ret

    def query2(self, l, r):
        return self.query1(r) - self.query1(l)

A.append(K + 1)
A.append(K + 1)
bit_tree = BIT(N + 2, A)
ANS = 0
S = 0
for i in range(N):
    l = i
    r = N + 2
    if bit_tree.query2(i, N) >= K:
        while r - l > 1:
            c = (l + r) // 2
            SUM = bit_tree.query2(i, c)
            if SUM >= K:
                r = c
            else:
                l = c
        ANS += N - l

print(ANS)