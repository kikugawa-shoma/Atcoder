A = int(input())
B = int(input())

ans = set([1, 2, 3])
ans.remove(A)
ans.remove(B)
a = 0
print(list(ans)[0])