S = input()

N = len(S)

def check(SS):
    L = len(SS)
    f = 0
    for i in range(L):
        if SS[i] != SS[L - i - 1]:
            f = 1
    if f == 1:
        return False
    else:
        return True


if check(S) and check(S[:(N-1)//2]) and check(S[(N+3)//2-1:]):
    print("Yes")
else:
    print("No")
