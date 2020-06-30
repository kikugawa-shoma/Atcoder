# 1-indexed　Binary Indexed Tree
class BIT:
    def __init__(self, n, init_list):
        self.num = n + 1
        self.tree = [0] * self.num
        for i, e in enumerate(init_list):
            self.update(i, e)

    #a_k?x???
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

    #???????????l????r?????
    def query2(self, l, r):
        return self.query1(r) - self.query1(l)