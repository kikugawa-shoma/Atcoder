N = int(input())
D = [int(d) for d in input().split()]

SUM_D = sum(D)
xy = 0
xx = 0
for d in D:
    xy += d * SUM_D
    xx += d * d

print((xy - xx)//2)


