N = int(input())
S = ["*"]*(N+1)
S[1:] = list(input())
Q = int(input())
q1,q2,q3 = [0]*Q,[0]*Q,[0]*Q
for i in range(Q):
    tmp = input().split()
    q1[i],q2[i] = map(int,tmp[:2])
    if q1[i] == 2:
        q3[i] = int(tmp[2])
    else:
        q3[i] = tmp[2]

class BIT:
    def __init__(self, n, init_list):
        self.num = n + 1
        self.tree = [0] * self.num
        for i, e in enumerate(init_list):
            self.update(i, e)

    #a_kにxを加算
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

    #通常のスライスと同じ。lは含み、rは含まない
    def query2(self, l, r):
        return self.query1(r) - self.query1(l)

s_pos = [BIT(N+1,[0]*(N+1)) for _ in range(26)]

for i in range(1,N+1):
    s_pos[ord(S[i]) - ord("a")].update(i,1)

alphabets = [chr(ord("a") + i) for i in range(26)]

for i in range(Q):
    if q1[i] == 1:
        s_pos[ord(S[q2[i]]) - ord("a")].update(q2[i],-1)
        S[q2[i]] = q3[i]
        s_pos[ord(q3[i]) - ord("a")].update(q2[i],1)
    else:
        ans = 0
        for c in alphabets:
            if s_pos[ord(c) - ord("a")].query2(q2[i],q3[i]+1) > 0:
                ans += 1
        print(ans)









