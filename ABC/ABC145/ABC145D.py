
X, Y = map(int, input().split())
mod = 10 ** 9 + 7


def prime_mod(n, m):
    S = 1
    for i in range(1, n+1):
        S *= i
        S %= m
    return S


def prime_inv_mod(n, m):
    invs = [0] * (n + 1)
    invs[1] = 1
    for i in range(2, n + 1):
        invs[i] = m - invs[m % i] * (m//i) % m
    return invs


a = 2 * Y - X
b = 2 * X - Y
if a % 3 != 0 or b % 3 != 0 or a < 0 or b < 0:
    print(0)
else:
    a //= 3
    b //= 3
    upper = prime_mod(a+b, mod)
    mod_inv = prime_inv_mod(max(a, b), mod)

    lower1 = 1
    lower2 = 1
    for i in range(1, a + 1):
        lower1 *= mod_inv[i]
        lower1 %= mod
    for i in range(1, b + 1):
        lower2 *= mod_inv[i]
        lower2 %= mod

    print((upper*lower1*lower2) % mod)






