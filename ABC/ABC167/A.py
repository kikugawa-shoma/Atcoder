S = input()
T = input()

n = len(S)
f = True
for i in range(n):
    if S[i] != T[i]:
        f = False


if f:
    print("Yes")
else:
    print("No")