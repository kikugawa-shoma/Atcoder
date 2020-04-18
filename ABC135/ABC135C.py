N = int(input())
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]
ans = 0
for i in range(N):
    remain_power = B[i] - A[i]
    if remain_power <= 0:
        ans += B[i]
    else:
        ans += A[i]
        next_A = max(0, A[i+1] - remain_power)
        ans += A[i+1] - next_A
        A[i+1] = next_A
print(ans)


