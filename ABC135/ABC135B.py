N = int(input())
P = [int(p) for p in input().split()]

cnt = 0
for i in range(N):
    if P[i] != i + 1:
        cnt += 1

if cnt <= 2:
    print("YES")
else:
    print("NO")
