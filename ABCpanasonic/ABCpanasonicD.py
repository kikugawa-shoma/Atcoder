N = int(input())
ans = []


def next_chr(ch):
    res = []
    g = ord(ch) - ord("a") + 2
    for i in range(g):
        res.append(chr(ord("a")+i))
    return res


def answer(s, i):
    if i == N:
        ch = next_chr(max(s))
        for m in ch:
            ans.append("".join([s, m]))
    else:
        i += 1
        ch = next_chr(max(s))
        for m in ch:
            answer("".join([s, m]), i)


if N == 1:
    print("a")
else:
    answer("a", 2)
    ans = sorted(ans)
    for c in ans:
        print(c)







