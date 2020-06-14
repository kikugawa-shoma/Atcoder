N, K, Q = map(int, input().split())
A = [int(input()) for q in range(Q)]

acc = [0]*N
for a in A:
    acc[a-1] += 1

for corr_num in acc:
    if K - (Q - corr_num) <= 0:
        print("No")
    else:
        print("Yes")
