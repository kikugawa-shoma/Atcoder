N = int(input())


def DFS(N, S):
    if len(S) == N:
        print(S)
    else:
        if S:
            next_max_chr = ord(max(S)) + 1
        else:
            next_max_chr = ord("a")
        for i in range(0, next_max_chr - ord("a") + 1):
            DFS(N, S + chr(ord("a") + i))


DFS(N, "")
