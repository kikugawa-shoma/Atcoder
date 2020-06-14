N = int(input())
P = [int(p) for p in input().split()]
Q = [int(q) for q in input().split()]

fact = [1] * (N+1)
for i in range(2,N+1):
    fact[i] = fact[i-1]*i


def dic_num(S):
    keta = 0
    num = 0
    S_set = set()
    for i in range(len(S)):
        minor = 0
        for j in S_set:
            if S[keta] > j:
                minor = minor + 1
        num += (S[keta] - 1 - minor) * fact[len(S)-keta-1]
        S_set.add(S[keta])
        keta += 1

    return num+1


print(abs(dic_num(P)-dic_num(Q)))






