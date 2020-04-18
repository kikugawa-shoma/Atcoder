"""
5 20
10 14 19 34 33

5 21
10 14 19 34 33

5 3
10 14 19 34 33
"""
# 累積和を計算するモジュール
from itertools import accumulate
# 二分探索モジュール
from bisect import bisect_left

#n, m, *a = map(int, sys.stdin.read().split())
n, m = map(int, input().split())
a = [int(ai) for ai in input().split()]
a.sort()


def f(x):
    # 幸福度がx未満となる組み合わせの個数を数える
    # ここも二分探索。言い換え。「xとA[i]+A[j]を比較　＝　x-A[i]とA[j]を比較」
    cnt = 0
    for ai in a:
        cnt += bisect_left(a, x - ai)
    # 幸福度がx以上の組み合わせの個数がm未満かどうか
    return n * n - cnt < m

# 最小と最大はこれ。両端にして二分探索
left = a[0] * 2
right = a[-1] * 2
while right - left > 1:
    mid = (right + left) // 2
    if f(mid):
        right = mid
    else:
        left = mid
ans = 0
# 累積和を計算。和の計算に使用
cumsum = [0] + list(accumulate(a))
j = 0
for ai in a:
    i = bisect_left(a, left - ai)
    # 何個採用されたかをjでカウント
    j += n - i
    # 答えを累積和を使って計算
    ans += ai * (n - i) + cumsum[-1] - cumsum[i]
# 足しすぎた分を引く。
ans += (m - j) * left
print(ans)