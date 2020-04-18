""""
3 5
...#.
.#.#.
.#...
"""
from collections import deque
import numpy as np

H, W = map(int, input().split())
Map = [list(input()) for i in range(H)]


def make_wall(W, Map):
    for map_row in Map:
        map_row.append("#")
        map_row.insert(0, "#")

    wall = ["#"]*(W+2)
    Map.append(wall)
    Map.insert(0, wall)
    return Map


start_list = deque()
search_list = deque()
Map = make_wall(W, Map)
H += 2
W += 2

start_h = 0
for h in range(H):
    start_w = 0
    for w in range(W):
        if Map[h][w] == ".":
            start_list.append([start_h, start_w])
        start_w += 1
    start_h += 1



max_cost = 0
while start_list != deque():
    search_list.append(start_list.popleft())
    cost_map = np.array([[0] * W for i in range(H)])
    search_map = np.array([[0] * W for i in range(H)])

    while search_list != deque():
        tmp = search_list.popleft()
        x = tmp[0]
        y = tmp[1]
        search_map[x][y] = 1
        if Map[x][y+1] == "." and search_map[x][y+1] == 0 and [x, y+1] not in search_list:
            search_list.append([x, y+1])
            cost_map[x][y+1] = cost_map[x][y]+1
        if Map[x][y-1] == "." and search_map[x][y-1] == 0 and [x, y-1] not in search_list:
            search_list.append([x, y-1])
            cost_map[x][y-1] = cost_map[x][y]+1
        if Map[x+1][y] == "." and search_map[x+1][y] == 0 and [x+1, y] not in search_list:
            search_list.append([x+1, y])
            cost_map[x+1][y] = cost_map[x][y]+1
        if Map[x-1][y] == "." and search_map[x-1][y] == 0 and [x-1, y] not in search_list:
            search_list.append([x-1, y])
            cost_map[x-1][y] = cost_map[x][y]+1
    cost_map = np.array(cost_map)
    if max_cost < np.amax(cost_map):
        max_cost = np.amax(cost_map)

print(max_cost)

"""
20 20
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
"""