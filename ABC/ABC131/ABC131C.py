from math import gcd

A, B, C, D = map(int, input().split())
N = B - A + 1
lcm_CD = (C * D) // gcd(C, D)

sumB = B - B // C - B // D + B // lcm_CD
sumA = (A - 1) - (A - 1) // C - (A - 1) // D + (A - 1) // lcm_CD

print(sumB - sumA)
