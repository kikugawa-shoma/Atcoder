A, B, X = map(int, input().split())

for d in range(10, 0, -1):
    min_money = A * (10**(d-1)) + B * d
    if min_money <= X:
        break

if d != 10:
    N = (X - B * d) // A
    if N >= 10**d:
        print(int(format("", "9>{}".format(d))))
    elif N >= 1:
        print(N)
    else:
        print(0)

if d == 10:
    print(10**9)


