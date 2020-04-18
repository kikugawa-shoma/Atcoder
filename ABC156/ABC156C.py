N = int(input())
X = [int(x) for x in input().split()]

INF = (100 ** 2) * 100

minD = INF

for xi in range(1, 101):
    D = 0
    for n in range(N):
        D += (xi-X[n])**2
    if D < minD:
        minD = D

print(minD)


