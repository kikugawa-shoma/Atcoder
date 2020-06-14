S = input()

if len(S)%2==1:
    S1 = S[:len(S)//2]
    S2 = S[(len(S)//2)+1:]
else:
    S1 = S[:len(S)//2]
    S2 = S[(len(S)//2):]

hug = 0
for i in range(len(S1)):
    if S1[i] != S2[-(i+1)]:
        hug += 1

print(hug)
