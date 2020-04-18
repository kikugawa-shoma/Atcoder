N = int(input())
ST = input().split()
S = ST[0]
T = ST[1]

STR = ""
for i in range(N):
    STR = "".join([STR, S[i]])
    STR = "".join([STR, T[i]])

print(STR)
