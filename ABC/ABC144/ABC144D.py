import math

a, b, x = map(int, input().split())

V = a*a*b

if x >= V/2:
    print(math.degrees(math.atan(2*(V-x)/(a**3))))

else:
    print(90-math.degrees(math.atan(2*x/((b**2)*a))))


