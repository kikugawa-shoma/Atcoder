# -*- coding: euc-jp -*-
"""mod m での1!,2!,3!,...,n!とその逆元全てをO(n)で計算するライブラリ
"""

# 1!,2!,3!,...,n! (mod m)
def mod_factorials(n, m):
    mod_factorials = [1] * (n + 1)
    for i in range(1, n+1):
        mod_factorials[i] = mod_factorials[i-1]*i
        mod_factorials[i] %= m
    return mod_factorials

# 1!,2!,3!,...,n! の逆元 (mod m)
def mod_inv_factorials(n, m):
    mod_invs = [1] * (n + 1)
    invs = [1] * (n + 1)
    for i in range(2, n + 1):
        invs[i] = m - invs[m % i] * (m//i) % m

    for i in range(1, n+1):
        mod_invs[i] = invs[i]*mod_invs[i-1]
        mod_invs[i] %= m
    return mod_invs

"""
A = mod_factorials(10,10**9+7)
B = mod_inv_factorials(10,10**9+7)
print(A)
print(B)
>[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
>[1, 1, 500000004, 166666668, 41666667, 808333339, 301388891, 900198419, 487524805, 831947206, 283194722]
"""