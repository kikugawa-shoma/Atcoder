T = list(input())

n = len(T)
T.append("P")
T.insert(0,"D")


ans = []
for i in range(1,n+1):
    if T[i] == "?":
        if T[i-1] == "P":
            T[i] = "D"
        elif T[i-1] == "D":
            T[i] = "D"

print("".join(T[1:n+1]))


