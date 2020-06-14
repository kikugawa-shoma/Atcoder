
N = int(input())
AB = [[0] * 2 for _ in range(N)]
time = [0] * N
out = 0
q = []
for i in range(N):
    tmp = list(map(int, input().split()))
    AB[i][0] = tmp[0]
    AB[i][1] = tmp[1]
    if AB[i][1] - AB[i][0] < 0:
        out = 1

AB = sorted(AB, key=lambda x: x[1])

count = 0
for i in range(N):
    if count + AB[i][0] > AB[i][1]:
        out = 1
        break
    else:
        count += AB[i][0]
if out == 0:
    print("Yes")
else:
    print("No")


