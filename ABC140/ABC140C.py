N = int(input())
B = [int(b) for b in input().split()]

ans = B[0] + B[-1]
for i in range(0, N-2):
    ans += min(B[i], B[i+1])

print(ans)
