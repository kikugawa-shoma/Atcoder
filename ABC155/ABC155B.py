N = int(input())
A = [int(i) for i in input().split()]

f = 0
for a in A:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            f = 1

if f == 1:
    print("DENIED")
else:
    print("APPROVED")


