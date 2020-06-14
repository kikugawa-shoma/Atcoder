A, B = map(int, input().split())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


A = set(make_divisors(A))
B = set(make_divisors(B))
C = A & B

cnt = 0
for i in C:
    if len(make_divisors(i)) == 1 or len(make_divisors(i)) == 2:
        cnt += 1
print(cnt)
