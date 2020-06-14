N, M = map(int, input().split())

if M == 0 or N == 0:
    print("{} {}".format(0, 0))
else:

    p = [0]*M
    S = [0]*M

    for i in range(M):
        tmp = input().split()
        p[i] = int(tmp[0])
        S[i] = tmp[1]

    penalty = 0


    correct_set = set()
    for i in range(M):
        if S[i] == 'AC':
            correct_set.add(p[i])

    correct = len(correct_set)

    for i in range(M):
        if S[i] == 'AC' and p[i] in correct_set:
            correct_set.remove(p[i])
        elif S[i] == 'WA' and p[i] in correct_set:
            penalty += 1
    print("{} {}".format(correct, penalty))