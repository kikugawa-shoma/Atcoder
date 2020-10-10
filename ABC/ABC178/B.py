a,b,c,d = map(int,input().split())

A = [0]*4
A[0] = a*c
A[1] = a*d
A[2] = b*c
A[3] = b*d
print(max(A))
