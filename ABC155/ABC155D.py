"""
4 3
3 4 -4 -2
6 3
1 2 3 -1 -2 -3
"""

N, K = map(int, input().split())
A = [int(a) for a in input().split()]
A.sort()

for i, a in enumerate(A):
    if a >= 0:
        break
A_minus = A[:i]
A_plus = A[i:]
mi_len = len(A_minus)
pl_len = len(A_plus)

nl = mi_len * pl_len
pl = (pl_len * (pl_len - 1) + mi_len * (mi_len - 1)) // 2


def count_minor1(Th):
    A_m = list(reversed(A_minus))
    A_p = list(reversed(A_plus))
    start = 0
    count = 0
    for i in range(pl_len):
        for j in range(start, mi_len):
            if A_m[j] * A_p[i] < Th:
                start = j
                count += mi_len - j
                break
    return count


def count_minor2(Th):
    A_abs = A_plus
    L = len(A_abs)
    count = 0
    start = 0
    for i in range(L-1, -1, -1):
        for j in range(start, L):
            if A_abs[i] * A_abs[j] >= Th:
                if i <= j-1:
                    count += j - 1
                else:
                    count += j
                start = j
                break
        else:
            count += L-1
    A_abs = [abs(a) for a in A_minus]
    A_abs.sort()
    L = len(A_abs)
    start = 0
    for i in range(L-1, -1, -1):
        for j in range(start, L):
            if A_abs[i] * A_abs[j] >= Th:
                if i <= j-1:
                    count += j - 1
                else:
                    count += j
                start = j
                break
        else:
            count += L-1
    return count//2


if K <= nl:
    lower = -10**18+10
    upper = 0
    while upper-lower > 1:
        S = (lower + upper) // 2
        if count_minor1(S) > K:
            upper = S
        else:
            lower = S

else:
    K_ = K - nl
    upper = 10**18+10
    lower = 0
    while upper-lower > 1:
        S = (lower + upper) // 2
        if count_minor2(S) >= K_:
            upper = S
        else:
            lower = S
    print(lower)
