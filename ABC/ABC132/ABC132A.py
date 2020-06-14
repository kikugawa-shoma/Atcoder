from collections import defaultdict
S = input()

d = defaultdict(int)

for i in range(len(S)):
    d[S[i]] += 1
f = 0
for i in range(len(S)):
    if d[S[i]] != 2:
        f = 1

if f == 0:
    print("Yes")
else:
    print("No")


