N, K = map(int, input().split())

i = 0
while 1:
    if K ** (i+1) > N >= K ** i:
        break
    i += 1

print(i+1)

