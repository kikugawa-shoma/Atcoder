A,B,C,K = map(int,input().split())

if K <= A + B:
    print(min(A,K))
else:
    print(A-(K-A-B))