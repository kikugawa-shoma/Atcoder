import heapq as hq

H,W,K = map(int,input().split())
H = H+2
W = W+2
sx,sy,gx,gy = map(int,input().split())
sx,sy = sy,sx
gx,gy = gy,gx
inf = 10**7

M = [["@"]*W for _ in range(H)]

for h in range(1,H-1):
    M[h][1:-1] = list(input())

dist = [[[[inf,inf] for ___ in range(4)] for _ in range(W)] for __ in range(H)]
visited = [[[False for ___ in range(4)] for _ in range(W)] for __ in range(H)]
movable_state = 0
for h in range(H):
    for w in range(W):
        if M[h][w] == ".":
            movable_state += 4



for i in range(4):
    dist[sy][sx][i] = [0,0]

q = [[0,sx,sy,0],[0,sx,sy,1],[0,sx,sy,2],[0,sx,sy,3]]

def can_go(x,y):
    return M[y][x] == "."

def f(x):
    return x[0]*10**7+x[1]


while q != []:
    c,x,y,to = hq.heappop(q)
    swing,step = dist[y][x][to]
    if to == 0:
        if can_go(x-1,y):
            if step <= K-1:
                dist[y][x-1][0] = min([swing,step+1],dist[y][x-1][0],key=f)
                if not visited[y][x-1][0]:
                    hq.heappush(q,[f(dist[y][x-1][0]),x-1,y,0])
            else:
                dist[y][x-1][0] = min([swing+1,1],dist[y][x-1][0],key=f)
                if not visited[y][x-1][0]:
                    hq.heappush(q,[f(dist[y][x-1][0]),x-1,y,0])
        if can_go(x,y-1):
            dist[y-1][x][1] = min([swing+1,1],dist[y-1][x][1],key=f)
            if not visited[y-1][x][1]:
                hq.heappush(q,[f(dist[y-1][x][1]),x,y-1,1])
        if can_go(x+1,y):
            dist[y][x+1][2] = min([swing+1,1],dist[y][x+1][2],key=f)
            if not visited[y][x+1][2]:
                hq.heappush(q,[f(dist[y][x+1][2]),x+1,y,2])
        if can_go(x,y+1):
            dist[y+1][x][3] = min([swing+1,1],dist[y+1][x][3],key=f)
            if not visited[y+1][x][3]:
                hq.heappush(q,[f(dist[y+1][x][3]),x,y+1,3])
    if to == 1:
        if can_go(x,y-1):
            if step <= K-1:
                dist[y-1][x][1] = min([swing,step+1],dist[y-1][x][1],key=f)
                if not visited[y-1][x][1]:
                    hq.heappush(q,[f(dist[y-1][x][1]),x,y-1,1])
            else:
                dist[y-1][x][1] = min([swing+1,1],dist[y-1][x][1],key=f)
                if not visited[y-1][x][1]:
                    hq.heappush(q,[f(dist[y-1][x][1]),x,y-1,1])
        if can_go(x-1,y):
            dist[y][x-1][0] = min([swing+1,1],dist[y][x-1][0],key=f)
            if not visited[y][x-1][0]:
                hq.heappush(q,[f(dist[y][x-1][0]),x-1,y,0])
        if can_go(x+1,y):
            dist[y][x+1][2] = min([swing+1,1],dist[y][x+1][2],key=f)
            if not visited[y][x+1][2]:
                hq.heappush(q,[f(dist[y][x+1][2]),x+1,y,2])
        if can_go(x,y+1):
            dist[y+1][x][3] = min([swing+1,1],dist[y+1][x][3],key=f)
            if not visited[y+1][x][3]:
                hq.heappush(q,[f(dist[y+1][x][3]),x,y+1,3])
    
    if to == 2:
        if can_go(x+1,y):
            if step <= K-1:
                dist[y][x+1][2] = min([swing,step+1],dist[y][x+1][2],key=f)
                if not visited[y][x+1][2]:
                    hq.heappush(q,[f(dist[y][x+1][2]),x+1,y,2])
            if step == K:
                dist[y][x+1][2] = min([swing+1,1],dist[y][x+1][2],key=f)
                if not visited[y][x+1][2]:
                    hq.heappush(q,[f(dist[y][x+1][2]),x+1,y,2])
        
        if can_go(x-1,y):
            dist[y][x-1][0] = min([swing+1,1],dist[y][x-1][0],key=f)
            if not visited[y][x-1][0]:
                hq.heappush(q,[f(dist[y][x-1][0]),x-1,y,0])
        if can_go(x,y-1):
            dist[y-1][x][1] = min([swing+1,1],dist[y-1][x][1],key=f)
            if not visited[y-1][x][1]:
                hq.heappush(q,[f(dist[y-1][x][1]),x,y-1,1])
        if can_go(x,y+1):
            dist[y+1][x][3] = min([swing+1,1],dist[y+1][x][3],key=f)
            if not visited[y+1][x][3]:
                hq.heappush(q,[f(dist[y+1][x][3]),x,y+1,3])
    
    if to == 3:
        if can_go(x,y+1):
            if step <= K-1:
                dist[y+1][x][3] = min([swing,step+1],dist[y+1][x][3],key=f)
                if not visited[y+1][x][3]:
                    hq.heappush(q,[f(dist[y+1][x][3]),x,y+1,3])
            else:
                dist[y+1][x][3] = min([swing+1,1],dist[y+1][x][3],key=f)
                if not visited[y+1][x][3]:
                    hq.heappush(q,[f(dist[y+1][x][3]),x,y+1,3])
        if can_go(x-1,y):
            dist[y][x-1][0] = min([swing+1,1],dist[y][x-1][0],key=f)
            if not visited[y][x-1][0]:
                hq.heappush(q,[f(dist[y][x-1][0]),x-1,y,0])
        if can_go(x,y-1):
            dist[y-1][x][1] = min([swing+1,1],dist[y-1][x][1],key=f)
            if not visited[y-1][x][1]:
                hq.heappush(q,[f(dist[y-1][x][1]),x,y-1,1])
        if can_go(x+1,y):
            dist[y][x+1][2] = min([swing+1,1],dist[y][x+1][2],key=f)
            if not visited[y][x+1][2]:
                hq.heappush(q,[f(dist[y][x+1][2]),x+1,y,2])
    visited[y][x][to] = True

if (visited[gy][gx][0] | visited[gy][gx][1] | visited[gy][gx][2] | visited[gy][gx][3]) == False:
    print(-1)
    exit()
print(min(dist[gy][gx][0][0],dist[gy][gx][1][0],dist[gy][gx][2][0],dist[gy][gx][3][0])+1)

"""
for h in range(H):
    for w in range(W):
        m = inf
        for i in range(4):
            m = min(m,dist[h][w][i][0])
        print(m,end=" ")
    print("\n")
"""

            








