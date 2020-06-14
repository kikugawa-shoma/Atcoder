N = int(input())
A = [int(a) for a in input().split()]

ans = 0
for a in A:
    ans += 1 / a

print(1 / ans)