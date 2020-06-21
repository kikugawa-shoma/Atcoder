"""
これだと
A = [1,1,1,1,...,1,1000000]
のときにTLEしてしまう。
A[i] = 1のときの計算量はmax(A) = 10**6
これをN回繰り返すのでTLEする。（ただしオンラインジャッジはテストケースが弱いので通る）

このTLEを回避するにはすでに計算したA[i]と同じ値に対しては計算をしない工夫が必要。
これをD_re2.pyにて実装してある。
"""

import bisect as bc
 
N = int(input())
A = list(map(int,input().split()))
A.sort()
 
dp = [True for _ in range(A[-1]+1)]
 
for i in range(N):
    ai = A[i]
    for j in range(2,A[-1]+1):
        if ai*j > A[-1]:
            break
        dp[ai*j] = False
ans = 0
for i in range(N):
    if dp[A[i]]:
        if bc.bisect_right(A,A[i]) - bc.bisect_left(A,A[i]) == 1:
            ans += 1
 
print(ans)