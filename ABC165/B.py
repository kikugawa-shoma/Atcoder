X=int(input())
money=100
year=0

while 1:
    year += 1
    money*=1.01
    money=int(money)
    if money >= X:
        break

print(year)