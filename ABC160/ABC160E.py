X, Y, A, B, C = map(int, input().split())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
P.sort()
Q.sort()
P.reverse()
Q.reverse()

P = P[:X]
Q = Q[:Y]

eatable_apple = P+Q+R
eatable_apple.sort()
eatable_apple.reverse()

print(sum(eatable_apple[:X+Y]))
