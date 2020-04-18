from collections import Counter

N, P = map(int, input().split())
S = [int(s) for s in input()]
S.reverse()

ans = 0

if P != 2 and P != 5:
    prime10 = [1] * N
    for n in range(1, N):
        prime10[n] = (prime10[n-1] * 10) % P
    S = [(s * prime10[n]) % P for n, s in enumerate(S)]
    for n in range(1, N):
        S[n] = (S[n-1] + S[n]) % P

    S = Counter(S)
    for p in range(P):
        if p == 0:
            ans += S[p]
        ans += (S[p] * (S[p]-1)) // 2

else:
    for n in range(N):
        if S[n] % P == 0:
            ans += N - n

print(ans)
