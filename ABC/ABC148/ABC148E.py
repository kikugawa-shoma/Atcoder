
N = int(input())

if N % 2 == 1:
    print(0)
else:
    beki5 = 1
    sum0 = 0
    while 1:
        beki5 = beki5 * 5
        if beki5 > N:
            break
        else:
            sum0 += N//(beki5*2)
    print(sum0)
