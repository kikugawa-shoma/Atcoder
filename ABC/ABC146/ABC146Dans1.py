import sys

input = sys.stdin.readline
N = int(input());
AB = [tuple(map(int, input().split())) for _ in range(1, N)]

co = [0 for _ in range(N)]
prev = 0
color = 1
for a, b in sorted(AB):
    if prev != a:
        color = 1
    if co[a - 1] == color:
        color += 1
    co[b - 1] = color
    prev = a
    color += 1

print(max(co))
for _, b in AB:
    print(co[b - 1])