import math
A,B,H,M = map(int,input().split())

theta = abs(30*H+M/2-6*M)
if theta == 180:
    print(A+B)
else:
    if theta > 180:
        theta = 360-theta

    theta = math.radians(theta)
    print((A**2+B**2-2*A*B*math.cos(theta))**0.5)
