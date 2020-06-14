import sys, math

input = sys.stdin.readline

mod = 10 ** 9 + 7

n = int(input())
lst_a = list(map(int, input().split()))

lcm = 1
for a in lst_a:
    lcm = a * lcm // math.gcd(a, lcm)
lcm %= mod
ans = 0
for a in lst_a:
    ans += lcm * pow(a, mod - 2, mod)
    ans %= mod

print(ans)