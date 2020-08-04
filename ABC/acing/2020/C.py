from collections import defaultdict

N = int(input())

d = defaultdict(int)

for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100):
            n = x**2+y**2+z**2+x*y+y*z+z*x
            if x == y == z:
                d[n] += 1
            elif x == y or y == z or z == x:
                d[n] += 3
            else:
                d[n] += 6
            
            if n > N:
                break

for i in range(1,N+1):
    print(d[i])

