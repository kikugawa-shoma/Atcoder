N = int(input())
a = [int(aa) for aa in input().split()]

cnt = 1
for now_a in a:
    if cnt == now_a:
        cnt += 1

if cnt == 1:
    print(-1)
else:
    print(N - cnt + 1)