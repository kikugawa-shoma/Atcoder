H, W = map(int, input().split())

base = W // 2
if H == 1 or W == 1:
    print(1)
elif W % 2 == 1:
    print(base*H + (H - 1) // 2 + 1)
else:
    print(base*H)