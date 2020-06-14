A = [int(a) for a in input().split()]

sumA = sum(A)
if sumA >= 22:
    print("bust")
else:
    print("win")