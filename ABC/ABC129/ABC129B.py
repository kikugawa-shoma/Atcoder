N = int(input())
W = list(map(int, input().split()))

S1 = W[0]
S2 = sum(W[1:])
abs_min = abs(S1-S2)

for i in range(1, N-1):
    S1 += W[i]
    S2 -= W[i]
    abs_min = min(abs_min, abs(S1-S2))

print(abs_min)



