S = input()

f = 0
for i in range(3):
    if S[i] == S[i + 1]:
        f = 1
        break
if f == 1:
    print("Bad")
else:
    print("Good")
