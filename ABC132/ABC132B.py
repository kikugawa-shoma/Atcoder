n = int(input())
P = list(map(int, input().split()))

cnt = 0
for i in range(1, n - 1):
    f = 0
    if P[i - 1] < P[i] and P[i] < P[i + 1]:
        f = 1
    elif P[i -1] > P[i] and P[i] > P[i + 1]:
        f = 1
    if f == 1:
        cnt += 1

print(cnt)
