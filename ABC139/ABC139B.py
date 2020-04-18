A, B = map(int, input().split())


tap = 1
num = 0
while 1:
    if tap >= B:
        print(num)
        break
    tap += A - 1
    num += 1


