S = input()

for i in range(1, len(S)+1):
    if i%2 == 1:
        if S[i-1] == "L":
            print("No")
            break
    else:
        if S[i-1] == "R":
            print("No")
            break
else:
    print("Yes")
