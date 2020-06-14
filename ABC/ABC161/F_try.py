N = int(input())
l = []
for n in range(2,N+1):
    tmp_N = N 
    while 1:
        if tmp_N >= n:
            if tmp_N%n==0:  
                tmp_N = tmp_N // n
            else:
                tmp_N = tmp_N - n
        else:
            if tmp_N == 1:
                l.append(n)
            break

print(l)

