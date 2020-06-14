n, a, b = map(int, input().split())

mod = 10 **9 +7
kinds = 0

def mod_factorial(nr, nl, m):
    r = 1
    for i in range(nl+1, nr+1):
        r *= i
        r %= m
    return r


def mod_inv_factorial(n1, n2, m):
    n = max(n1, n2)
    invs = [0] * (n + 1)
    invs[1] = 1
    for i in range(2, n + 1):
        invs[i] = m - invs[m % i] * (m//i) % m

    r1 = 1
    r2 = 1
    for i in range(1, n1+1):
        r1 *= invs[i]
        r1 %= m
    for i in range(1, n2+1):
        r2 *= invs[i]
        r2 %= m
    return r1, r2


kinds = 2 ** n - 1

la = max(a, n-a)
sa = min(a, n-a)
lb = max(b, n-b)
sb = min(b, n-b)

upper1 = mod_factorial(n, la, mod)
upper2 = mod_factorial(n, lb, mod)

r1, r2 = mod_inv_factorial(sa, sb, mod)

print((kinds - upper1 * r1 - upper2 * r2) % mod)
