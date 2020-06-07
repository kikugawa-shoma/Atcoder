H1,M1,H2,M2,K = map(int,input().split())

t1 = H1*60+M1
t2 = H2*60+M2
dt = t2-t1

print(max(dt-K,0))