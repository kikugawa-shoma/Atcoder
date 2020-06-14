
X,Y = map(int,input().split())
f = False

for a in range(101):
    for b in range(101):
        if a+b == X and 2*a+4*b == Y:
            f = True
            break

if f:
    print("Yes")
else:
    print("No")
