N = int(input())
H = [int(h) for h in input().split()]
f = 0
for n in range(N-1, 0, -1):
    if H[n] < H[n-1]:
        H[n-1] -= 1
        if H[n] < H[n-1]:
            print("No")
            break

else:
    print("Yes")
