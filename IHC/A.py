D = int(input())
C = [0]*27
C[1:] = list(map(int,input().split()))
S = [[0]*27 for _ in range(D+1)]
for i in range(1,D+1):
    S[i][1:] = list(map(int,input().split()))