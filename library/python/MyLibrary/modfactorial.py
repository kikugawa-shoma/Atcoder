# nの階乗をmod mで返す
def mod_factorial(n, m):
    r = 1
    for i in range(1, n+1):
        r *= i
        r %= m
    return r

# n1とn2のmod での階乗の逆元を返す関数
def mod_inv_factorial2(n1, n2, m):
    n = max(n1, n2)
    invs = [0] * (n + 1)
    invs[1] = 1
    for i in range(2, n + 1):
        invs[i] = m - invs[m % i] * (m//i) % m

    r1 = r2 = 1
    for i in range(1, n+1):
        r1 *= invs[i]
        r1 %= m
        if i == min(n1, n2):
            r2 = r1
    return r1, r2

# nのmod での階乗の逆元を返す関数
def mod_inv_factorial1(n, m):
    invs = [0] * (n + 1)
    invs[1] = 1
    for i in range(2, n + 1):
        invs[i] = m - invs[m % i] * (m//i) % m

    r = 1
    for i in range(1, n+1):
        r *= invs[i]
        r %= m
    return r

