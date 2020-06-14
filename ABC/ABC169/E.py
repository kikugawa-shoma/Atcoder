N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i],B[i] = map(int,input().split())
A.sort()
B.sort()

if N % 2 == 1:
    mid_ind = N//2
    lower = A[mid_ind]
    upper = B[mid_ind]
    print(upper-lower+1)

else:
    mid_a = N//2
    mid_b = mid_a-1
    lower = (A[mid_a]+A[mid_b])/2
    upper = (B[mid_a]+B[mid_b])/2
    print(int((upper-lower)*2+1))

