N = int(input())
A = [int(a) for a in input().split()]


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


divisor = []
for i in range(1, N + 1):
    divisor.append(make_divisors(i))
B = [0]*N
rs = [0]*N
for i in range(N - 1, -1, -1):
    if rs[i] != A[i]:
        B[i] = 1
        for j in divisor[i]:
            rs[j-1] = 1 - rs[j-1]

print(sum(B))
for i in range(N):
    if B[i] == 1:
        print(i+1)
