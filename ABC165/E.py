N,M=map(int,input().split())

if N%2 == 1:
    left=N//2
    right=left+2
    for i in range(M):
        print("{} {}".format(left,right))
        left -= 1
        right += 1

else:
    left=N//2
    right=left+1
    for i in range(M):
        print("{} {}".format(left,right))
        left -= 1
        right += 1