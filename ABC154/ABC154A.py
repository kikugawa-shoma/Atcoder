ST = input().split(" ")
A, B = map(int, input().split())
U = input()

if U == ST[0]:
    A -= 1
else:
    B -= 1


print("{} {}".format(A, B))

