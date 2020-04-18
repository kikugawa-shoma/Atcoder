N = int(input())
A = [int(a) for a in input().split()]

setA = set(A)
if len(setA) == len(A):
    print("YES")
else:
    print("NO")






