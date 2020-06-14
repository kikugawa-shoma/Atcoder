A = [0]*3
for i in range(3):
    A[i] = [int(a) for a in input().split()]

N = int(input())
B = [int(input()) for _ in range(N)]

for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = 0

f = 0
for i in range(3):
    if sum(A[i][:]) == 0:
        f = 1


for i in range(3):
    x = 0
    for j in range(3):
        x += A[j][i]
    if x == 0:
        f = 1
x = 0
for i in range(3):
    x += A[i][i]
if x == 0:
    f = 1

x = 0
x = A[0][2]+A[1][1]+A[2][0]
if x == 0:
    f = 1

if f == 1:
    print("Yes")
else:
    print("No")





