N, K = map(int, input().split())

if K > (N-1)*(N-2) // 2:
    print(-1)
else:
    max_dif = (N-1)*(N-2) // 2 - K
    M = N - 1 + max_dif
    print(M)
    for i in range(N-1):
        print("{} {}".format(1, i+2))
    node1 = 2
    node2 = 3
    for i in range(max_dif):
        print("{} {}".format(node1, node2))
        if node2 == N:
            node1 += 1
            node2 = node1 + 1
        else:
            node2 += 1

