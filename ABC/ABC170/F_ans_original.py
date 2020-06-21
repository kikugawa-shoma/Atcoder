import sys
import numpy as np
from heapq import heappop, heappush
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main(C, H, W, S, T, K):
    INF = 10**18
    N = H * W
    q = [5 * S]
    dist = np.full((5 * N), INF, np.int64)
    dist[5 * S] = 0
    move = [0, 1, -1, W, -W]
    B = 5 * N + 10
    while q:
        x = heappop(q)
        dist_x, x = divmod(x, B)
        if dist_x > dist[x]:
            continue
        v, d = divmod(x, 5)
        if d == 0:
            # どちらかに進む
            for i in range(1, 5):
                w = v + move[i]
                y = 5 * w + i
                dist_y = dist_x + 1
                if C[w] and dist_y < dist[y]:
                    dist[y] = dist_y
                    heappush(q, B * dist_y + y)
        else:
            # 直進する
            if dist_x % K != 0:
                w = v + move[d]
                y = 5 * w + d
                dist_y = dist_x + 1
                if C[w] and dist_y < dist[y]:
                    dist[y] = dist_y
                    heappush(q, B * dist_y + y)
            # 止まって向きを変える権利を得る
            y = 5 * v
            dist_y = dist_x + (-dist_x) % K
            if dist_y < dist[y]:
                dist[y] = dist_y
                heappush(q, B * dist_y + y)
    x = dist[5 * T]
    if x == INF:
        return -1
    return dist[5 * T] // K
 
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', '(b1[:],i8,i8,i8,i8,i8)')(main)
    cc.compile()
    exit()
from my_module import main
 
H, W, K = map(int, readline().split())
x1, y1, x2, y2 = map(int, readline().split())
 
C = np.zeros((H + 2, W + 2), np.bool_)
C[1:-1, 1:-1] = np.frombuffer(read(), 'S1').reshape(H, -1)[:, :W] == b'.'
C = C.ravel()
H += 2
W += 2
 
S = W * x1 + y1
T = W * x2 + y2
 
print(main(C, H, W, S, T, K))