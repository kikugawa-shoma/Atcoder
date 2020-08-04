from collections import defaultdict

K = int(input())

d = [0]*(K+1)

r = 0
ten = 1
while 1:
    r = (r+ten*7)%K
    ten *= 10
    ten %= K
    if r == 0:
        print(sum(d)+1)
        break
    if d[r] != 0:
        print(-1)
        break
    elif d[r] == 0:
        d[r] = 1



