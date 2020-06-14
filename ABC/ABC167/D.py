N,K = map(int,input().split())
A = list(map(int,input().split()))

A.insert(0,-1)

visited = [False]*(N+1)
now_town = 1
to_start = 0

while 1:
    if visited[now_town] == True:
        break
    else:
        visited[now_town] = True
        now_town = A[now_town]
        to_start += 1
roop_start = now_town

now_town = roop_start
roop = 0
while 1:
    roop += 1
    now_town = A[now_town]
    if now_town == roop_start:
        break

to_start -= roop

if K <= to_start:
    now_town = 1
    for i in range(K):
        now_town = A[now_town]
    print(now_town)
else:
    K -= to_start
    K %= roop
    now_town = roop_start
    for i in range(K):
        now_town = A[now_town]
    print(now_town)







