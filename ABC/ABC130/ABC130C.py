W, H, x, y = map(float, input().split())
f = 0
if W / 2 == x and H / 2 == y:
    f = 1

print("{} {}".format(W*H/2, f))

