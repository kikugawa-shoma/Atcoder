from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
N, M = map(int, input().split())
in_path = defaultdict(lambda: [])
out_path = defaultdict(lambda: [])

for m in range(M):
    x, y = map(int, input().split())
    in_path[y].append(x)
    out_path[x].append(y)

check = [False]*(N+1)
memo = [0]*(N+1)


def dp(i):
    if check[i]:
        return memo[i]
    else:
        check[i] = True
        if not out_path[i]:
            return 0
        else:
            max_path = 0
            for node in out_path[i]:
                max_path = max(dp(node), max_path)
            max_path += 1
            memo[i] = max_path
            return max_path


ans = 0
for i in range(1, N+1):
    ans = max(ans, dp(i))

print(ans)


