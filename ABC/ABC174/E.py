N,K = map(int,input().split())
A = list(map(int,input().split()))

def check(m):
    n = 0
    for a in A:
        if a%m == 0:
            n += a//m - 1
        else:
            n += a//m
    return n <= K
        

l = 0
r = 10**9+10

while r-l > 1:
    m = (r+l) // 2
    if check(m):
        r = m
    else:
        l = m

print(r)


