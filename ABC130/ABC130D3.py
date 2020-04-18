#尺取り法
N, K = map(int, input().split())
A = list(map(int, input().split()))
pre_head = 0
S = 0
ANS = 0
for tail in range(N):
    for head in range(pre_head, N):
        if S < K:
            S += A[head]
        if S >= K:
            S -= A[head]
            ANS += head - tail
            pre_head = head
            break
    else:
        tmp = head - tail + 1
        ANS += tmp*(1 + tmp)//2
        break
    S -= A[tail]
print((N+1)*N//2 - ANS)


