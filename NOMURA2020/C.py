N = int(input())
A = list(map(int,input().split()))

from_deeper_bind = [[0,0] for i in range(N+1)]
from_deeper_bind[N][0] = from_deeper_bind[N][1] = A[N]
node_num = [1]*(N+1)
node_num[N] = A[N]
from_shallower_bind = [1]*(N+1)

for i in range(N-1,-1,-1):
    from_deeper_bind[i][0],from_deeper_bind[i][1] = (from_deeper_bind[i+1][0]+1)//2+A[i],from_deeper_bind[i+1][1]+A[i]


if not from_deeper_bind[0][0] <= 1 <= from_deeper_bind[0][1]:
    print(-1)
    exit()


for i in range(1,N):
    from_shallower_bind[i] = (node_num[i-1]-A[i-1])*2
    node_num[i] = min(from_shallower_bind[i],from_deeper_bind[i][1])

print(sum(node_num))





