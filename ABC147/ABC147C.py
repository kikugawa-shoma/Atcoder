N = int(input())
x = [0] * N
y = [0] * N
A = [0] * N
for i in range(N):
    A[i] = int(input())
    x[i] = [0] * A[i]
    y[i] = [0] * A[i]
    for j in range(A[i]):
        x[i][j], y[i][j] = map(int, input().split())

x = [[x1-1 for x1 in x0] for x0 in x]

def check_honest():
    flag = True
    for ii in range(len(honest)):
        if int(honest[ii]) == 1:
            for jj in range(A[ii]):
                if int(honest[x[ii][jj]]) != y[ii][jj]:
                    flag = False
    return flag

max_sum = 0
for i in range(2**N):
    honest = bin(2**N | i)[3:]
    if check_honest():
        max_sum = max(max_sum, sum(list(map(int, list(honest)))))

print(max_sum)
