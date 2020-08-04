from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

kind = ["AC","WA","TLE","RE"]
d = defaultdict(int)
for i in range(N):
    d[S[i]] += 1

for i in range(len(kind)):
    print("{} x {}".format(kind[i],d[kind[i]]))


