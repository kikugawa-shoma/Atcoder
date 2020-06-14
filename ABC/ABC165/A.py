
K=int(input())
A,B=map(int,input().split())
f=False
k=K

while 1:
    if A <= k and k <=B:
        f=True
        break
    if B < k:
        break
    k+=K

if f:
    print("OK")
else:
    print("NG")

