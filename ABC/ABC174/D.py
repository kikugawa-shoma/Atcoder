N = int(input())

C = input()
firstW = -1
for i in range(N):
    if C[i] == "W":
        firstW = i
        break
for i in range(N-1,-1,-1):
    if C[i] == "R":
        firstR = i
        break

def checkR(ri,wi):
    for i in range(ri,wi,-1):
        if C[i] == "R":
            return i
    else:
        return -1

def checkW(ri,wi):
    for i in range(wi,ri):
        if C[i] == "W":
            return i
    else:
        return -1


if len(set(C)) == 1:
    print(0)
elif firstW > firstR:
    print(0)
else:
    ri = firstR
    wi = firstW
    cnt = 0
    while 1:
        wi = checkW(ri,wi+1)
        ri = checkR(ri-1,wi)
        if wi == -1 or ri == -1:
            break
        cnt += 1
    print(cnt+1)


        
