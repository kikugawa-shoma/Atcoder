N = int(input())
P = list(map(int, input().split()))

TF = [0]*200010

pointer = 0
for i in range(N):
    TF[P[i]] = 1
    while 1:
        if TF[pointer] == 0:
            print(pointer)
            break
        else:
            pointer += 1
