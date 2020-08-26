N = input()

L = len(N)

S = 0
for i in range(L):
    S += int(N[i])

if S % 9 == 0:
    print("Yes")
else:
    print("No")