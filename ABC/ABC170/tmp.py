import sys
import numpy as np
from heapq import heappop, heappush
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H,W,K = map(int,readline().split())
x1, y1, x2, y2 = map(int, readline().split())
 
C = np.zeros((H + 2, W + 2), np.bool_)
#C[1:-1, 1:-1] = np.frombuffer(read(), 'S1').reshape(H, -1)[:, :W] == b'.'
a = np.frombuffer(read(), 'S1')

print(a) 