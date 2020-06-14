import bisect

N = int(input())
D = sorted(list(map(int, input().split())))

if N % 2 == 1:
    print(0)
else:
    half = N // 2
    cnt = 0
    for k in range(0, 100005):
        if bisect.bisect_left(D, k) == half:
            cnt += 1
    print(cnt)



