N, L = map(int, input().split())

zero_apple = 100000
for i in range(1, N + 1):
    if abs(L + i - 1) < zero_apple:
        zero_apple = abs(L + i - 1)
        ind = i

taste = 0
for k in range(1, N + 1):
    if k != ind:
        taste += L + k - 1
print(taste)
