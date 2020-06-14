import bisect as bc
from collections import defaultdict
from collections import deque
N = int(input())
A = list(map(int,input().split()))
A.sort()
q = set([i for i in range(N)])
 
for i in range(N):
    ai = A[i]
    itr = list(q)
    for j in itr:
        if j == i:
            continue
        if A[j] % ai == 0:
            q.remove(j)
 
print(len(q))
 
 